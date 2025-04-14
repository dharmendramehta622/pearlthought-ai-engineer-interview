import os 
import google.generativeai as genai
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
from dotenv import load_dotenv
load_dotenv() 

# Configure Gemini API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Create a Gemini model (assuming you're using the latest text model)
model = genai.GenerativeModel("gemini-2.0-flash")

class PromptGenerator:
    
    def __init__(self):
        self.AZURE_OPENAI_ENDPOINT = os.getenv('AZURE_OPENAI_ENDPOINT')
        self.AZURE_OPENAI_KEY = os.getenv('AZURE_OPENAI_KEY')
        self.AZURE_OPENAI_DEPLOYMENT = os.getenv('AZURE_OPENAI_DEPLOYMENT')
        
    def generate_post(self,article_summary: str, perspectives: list) -> str:
        '''
        Generates a LinkedIn post (200–250 words) based on an article summary and key perspectives.

        Args:
            article_summary (str): A summary or URL of the article to reflect on.
            perspectives (list): A list of 5–7 key viewpoints that the post should incorporate.

        Returns:
            str: A first-person, physician-style LinkedIn post centered around "AI as an enabler".
        '''
        perspective_summary = "\n".join([f"- {p}" for p in perspectives])
        
        system_prompt = (
            "You are a physician thought leader with a passion for responsible, ethical AI adoption in healthcare. "
            "Your philosophy centers on 'AI as an enabler'—enhancing but not replacing human expertise.\n"
            "Generate a concise, insightful LinkedIn post (200-250 words) that reflects this mindset."
        )

        user_prompt = f"""
        Article Summary:
        {article_summary}

        Physician’s Core Viewpoints:
        {perspective_summary}

        Please write a post in first person that:
        - Summarizes your thoughts on the article
        - Reflects the above viewpoints
        - Ends with a thought-provoking question or CTA
        """

        # Generate the response
        response = model.generate_content(
            [
                {
                    "role": "user",
                    "parts": [
                        f"{system_prompt}\n\n{user_prompt}"
                    ]
                }
            ]
        )

        # Return the response text
        return response.text.strip()

    def calculate_confidence(self,text: str, perspectives: list) -> float:
        docs = [text] + perspectives
        vectorizer = TfidfVectorizer().fit_transform(docs)
        vectors = vectorizer.toarray()
        score = cosine_similarity([vectors[0]], vectors[1:]).mean()
        return round(score, 2)
