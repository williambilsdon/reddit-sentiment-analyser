import uvicorn
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

    reddit_client = Reddit(client_id="ZBOJsnxnu7IR0SiN8Z2T3g", client_secret="r8gFYgGI4IQ8RRHPfatqPuTWVdvUxQ", user_agent="wilsdon")
    print("created reddit client")

    comments = await reddit_client.GetComments(post_url)
    print("Collected comments now need to generate their sentiment")

    analyser = SentimentAnalyser(comments)
    return analyser.Analyse()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
