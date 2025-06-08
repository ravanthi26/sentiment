import streamlit as st
from textblob import TextBlob

st.title("📝 Sentiment Analysis Web App")

user_input = st.text_area("Enter a sentence or paragraph")

if st.button("Analyze"):
    blob = TextBlob(user_input)
    sentiment = blob.sentiment.polarity

    if sentiment > 0:
        st.success("✅ Positive Sentiment")
    elif sentiment < 0:
        st.error("❌ Negative Sentiment")
    else:
        st.info("😐 Neutral Sentiment")
