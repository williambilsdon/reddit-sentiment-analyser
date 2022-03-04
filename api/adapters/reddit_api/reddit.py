from re import sub
import asyncpraw
import json
from typing import List

class Reddit:
    def __init__(self, client_id: str, client_secret: str, user_agent: str) -> List[str]:
        self.client = asyncpraw.Reddit(
            client_id=client_id,
            client_secret=client_secret,
            user_agent=f'Comment Extraction (by u/{user_agent}',
        )

    async def GetComments(self, post_url: str) -> List[str]:
        submission = await self.client.submission(id=post_url)
        comments = await submission.comments()
        await comments.replace_more(limit=None)
        all_comments = await comments.list()

        return [comment.body for comment in all_comments]
