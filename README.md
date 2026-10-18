---

### project 2: `CodeAlpha_FAQChatbot`


# Chatbot for FAQs

An interactive FAQ Chatbot built using Python, Streamlit, NLTK, and Scikit-Learn to answer questions based on NLP preprocessing and cosine similarity matching[cite: 2, 15]. Developed for the CodeAlpha Artificial Intelligence Internship[cite: 1].

## Features
- **FAQ Dataset**: JSON-backed questions and answers related to internship guidelines[cite: 2, 15].
- **NLP Text Preprocessing**: Tokenization, text cleaning, lowercasing, and stop-word removal using NLTK[cite: 2, 15].
- **Cosine Similarity Matching**: Computes intent relevance using TF-IDF vectors and cosine similarity[cite: 2, 15].
- **Interactive Chat Interface**: Streamlit chat UI with dynamic message history (`st.chat_message`)[cite: 2, 15].

## Setup & Installation

1. Clone the repository:
   bash
   git clone [https://github.com/reethika1-ai/CodeAlpha_FAQChatbot.git](https://github.com/reethika1-ai/CodeAlpha_FAQChatbot.git)
   cd CodeAlpha_FAQChatbot

2.Install dependencies:
Bash
pip install -r requirements.txt

3.Run the application:
Bash
streamlit run app.py
