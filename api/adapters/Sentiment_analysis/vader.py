from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from typing import List


class SentimentAnalyser:
    def __init__(self, comments) -> None:
        self.comments = comments

    def Analyse(self) -> float:
        sentiment = 0
        analyser = SentimentIntensityAnalyzer()
        for comment in self.comments:
            sentiment += analyser.polarity_scores(comment)["compound"]

        return sentiment/len(self.comments)

