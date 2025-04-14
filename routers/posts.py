from fastapi import APIRouter
from models.posts import PostRequest,PostResponse
from genai_services import PromptGenerator
import os 

# Prompt generator object
prompt_generator = PromptGenerator()

# Create a Router 
router = APIRouter()


@router.post("/post", response_model=PostResponse)
async def generate_linkedin_post(data: PostRequest):
    post = prompt_generator.generate_post(data.article_summary, data.perspectives)
    score = prompt_generator.calculate_confidence(post, data.perspectives)
    return PostResponse(linkedin_post=post, confidence_score=score)