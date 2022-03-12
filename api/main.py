import uvicorn
import os
from adapters.Sentiment_analysis.vader import SentimentAnalyser
from adapters.reddit_api.reddit import Reddit

from fastapi import FastAPI, HTTPException
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
def root():
    return {"message": "Hello World"}

@app.get("/comments/{post_url}", response_model=float)
def get_comments(post_url):
    print("Entered Endpoint")

    reddit_client = Reddit(client_id=os.getenv('CLIENT_KEY'), client_secret=os.getenv('CLIENT_SECRET'), user_agent="wilsdon", post_url=post_url)
    print("created reddit client")

    comments, err = reddit_client.GetComments()
    if err != None:
        raise HTTPException(
            status_code=err, detail=f'Failed to genereate comments list for url: {post_url}'
        ) 
    print("Collected comments now need to generate their sentiment")

    try:
        analyser = SentimentAnalyser(comments)

        result = analyser.Analyse()
        #Converting -1 to 1 range into a percentage
        sentimentPercentage = ((result+1)/2) * 100
    except:
        raise HTTPException(
            status_code=500, detail=f'Unexpected error encountered when processing sentiment'
        ) 


    return sentimentPercentage

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
