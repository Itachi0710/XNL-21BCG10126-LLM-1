from transformers import pipeline

class SentimentAnalyzer:
    def __init__(self):
        self.sentiment_model = pipeline('sentiment-analysis')

    def analyze_sentiment(self, text):
        return self.sentiment_model(text)

    def analyze_market_sentiment(self, news_data):
        sentiment_scores = [self.analyze_sentiment(news) for news in news_data]
        return sentiment_scores
