from pydantic import BaseModel
from typing import List,Optional

class PostRequest(BaseModel):
    article_summary: str
    perspectives: List[str]  # 5-7 key views from client

class PostResponse(BaseModel):
    linkedin_post: str
    confidence_score: float