from fastapi import FastAPI,status
import openai
import os
from dotenv import load_dotenv
from routers import posts


load_dotenv()
openai.api_key = os.getenv("AZURE_OPENAI_KEY")
openai.api_base = os.getenv("AZURE_OPENAI_ENDPOINT")
openai.api_type = os.getenv("AZURE_API_TYPE")
openai.api_version = os.getenv("AZURE_API_VERSION")


app = FastAPI()

# Include the router
app.include_router(posts.router)


@app.get("/")
def read_root():
    return {
            "status":status.HTTP_200_OK,
            "message": "Hello from PearlThought",
        }
