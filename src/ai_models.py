from pydantic_ai import Agent
from pydantic_ai.models.groq import GroqModel
from pydantic_ai.providers.groq import GroqProvider

from src.config import settings
from src.schemas import EssayAIFeedback

model = GroqModel("mistral-saba-24b", provider=GroqProvider(api_key=settings.GROQ_API_KEY))
agent = Agent(model, output_type=EssayAIFeedback, instrument=True)
