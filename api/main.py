import uvicorn
import os
from adapters.Sentiment_analysis.vader import SentimentAnalyser
from adapters.reddit_api.reddit import Reddit

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Hellow World"}

@app.get("/comments/{post_url}", response_model=float)
async def get_comments(post_url):
    print("Entered Endpoint")

    reddit_client = Reddit(client_id=os.getenv('CLIENT_KEY'), client_secret=os.getenv('CLIENT_SECRET'), user_agent="wilsdon")
    print("created reddit client")

    comments = await reddit_client.GetComments(post_url)
    print("Collected comments now need to generate their sentiment")

    analyser = SentimentAnalyser(comments)

    result = analyser.Analyse()
    #Converting -1 to 1 range into a percentage
    sentimentPercentage = ((result+1)/2) * 100

    return sentimentPercentage

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
