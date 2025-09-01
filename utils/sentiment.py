# utils/sentiment.py
from litellm import LLM
from config import LLM_MODEL
from utils.logger import log

llm = LLM(model=LLM_MODEL)

def analyze_sentiment(text):
    try:
        prompt = f"Analyze the sentiment of the following text and explain why it might be viral:\n\n{text}"
        response = llm.generate(prompt)
        return response.text
    except Exception as e:
        log.error(f"Sentiment analysis failed: {e}")
        return "Sentiment analysis unavailable."