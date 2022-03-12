from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

def test_get_comments():
    response = client.get("/comments/tby02l")
    assert response.status_code == 200
    # Because this comment thread is live I cannot guaruntee the sentiment returned will always be matched
    # however I can be pretty confident if we get a 200 response we will have a sentiment 

def test_get_comments_bad_id():
    response = client.get("/comments/12345abc")
    assert response.status_code == 400

def test_get_comments_no_comments():
    #This is an old post I found on the /r/programming subreddit that shouldn't get any comment traction
    response = client.get("/comments/tav300")
    assert response.status_code == 500
