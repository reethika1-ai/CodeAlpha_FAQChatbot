import streamlit as st
import json
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

st.set_page_config(page_title="FAQ Chatbot", page_icon="🤖", layout="centered")

st.title("🤖 FAQ Chatbot")
st.write("Ask any question related to the internship guidelines or submission rules.")

# load FAQ dataset handling UTF-8 BOM encoding
@st.cache_data
def load_faqs():
    with open("faqs.json", "r", encoding="utf-8-sig") as file:
        return json.load(file)

faqs = load_faqs()
faq_questions = [item["question"] for item in faqs]
faq_answers = [item["answer"] for item in faqs]

# text preprocessing pipeline
def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    tokens = word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [word for word in tokens if word not in stop_words]
    return " ".join(filtered_tokens)

preprocessed_faqs = [preprocess_text(q) for q in faq_questions]

# session state memory
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello! I am your FAQ assistant. How can I help you today?"}
    ]

# render chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# process user input
if user_input := st.chat_input("Type your question here..."):
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)

    clean_user_input = preprocess_text(user_input)

    if not clean_user_input.strip():
        bot_response = "Please enter a clear question so I can assist you."
    else:
        vectorizer = TfidfVectorizer().fit(preprocessed_faqs + [clean_user_input])
        faq_vectors = vectorizer.transform(preprocessed_faqs)
        user_vector = vectorizer.transform([clean_user_input])

        similarities = cosine_similarity(user_vector, faq_vectors).flatten()
        best_match_idx = similarities.argmax()
        highest_similarity = similarities[best_match_idx]

        if highest_similarity > 0.2:
            bot_response = faq_answers[best_match_idx]
        else:
            bot_response = "I'm sorry, I couldn't find an answer to that. Please ask about internship tasks, submission steps, or certificates."

    st.session_state.messages.append({"role": "assistant", "content": bot_response})
    with st.chat_message("assistant"):
        st.write(bot_response)