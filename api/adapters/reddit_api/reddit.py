from distutils.log import error
import praw
from typing import List, Tuple

class Reddit:
    def __init__(self, client_id: str, client_secret: str, user_agent: str, post_url: str) -> List[str]:
        self.client = praw.Reddit(
            client_id=client_id,
            client_secret=client_secret,
            user_agent=f'Comment Extraction (by u/{user_agent}',
        )

        self.post_url=post_url

    def GetComments(self) -> Tuple[List[str], int]:
        try:
            submission = self.getPost()
        except:
            return None, 400

        try:
            all_comments = self.getComments(submission) 
        except:
            return None, 500

        return [comment.body for comment in all_comments], None

    def getPost(self):
        submission = self.client.submission(id=self.post_url)
        return submission

    def getComments(self, submission):
        submission.comments.replace_more(limit=None)
        all_comments = submission.comments.list()
        return all_comments
        
