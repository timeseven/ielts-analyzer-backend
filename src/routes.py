from fastapi import APIRouter

from src.ai_models import agent
from src.deps import RateLimitDep
from src.schemas import EssayInput, EssayResponse
from src.utils import custom_round_half

analyze_router = APIRouter()


@analyze_router.post("/analyze", response_model=EssayResponse)
async def analyze_essay(
    essay_input: EssayInput,
    rate_limit: RateLimitDep,
):
    instruction = """
        You are an IELTS writing examiner. Based on the question and essay provided, evaluate the writing across four
        IELTS criteria, and provide suggestions for improvement.

        Please return your results in the following structured format:
        - taskResponse: feedback + score
        - coherenceCohesion: feedback + score
        - lexicalResource: feedback + score
        - grammaticalRange: feedback + score
        - suggestions: 3–5 bullet-point suggestions for improvement

        Please note that scores should be between 0 and 9 with 0.5 increments.
        """
    prompt = f"Question: {essay_input.question}\nEssay: {essay_input.essay}\n{instruction}"
    response = await agent.run(prompt)
    result = response.output
    overallScore = custom_round_half(
        (
            result.taskResponse.score
            + result.coherenceCohesion.score
            + result.lexicalResource.score
            + result.grammaticalRange.score
        )
        / 4
    )

    return EssayResponse(overallScore=overallScore, **result.model_dump())
