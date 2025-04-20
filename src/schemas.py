from pydantic import BaseModel


class EssayInput(BaseModel):
    question: str
    essay: str


class ScoreAndFeedback(BaseModel):
    score: float
    feedback: str


class EssayAIFeedback(BaseModel):
    taskResponse: ScoreAndFeedback
    coherenceCohesion: ScoreAndFeedback
    lexicalResource: ScoreAndFeedback
    grammaticalRange: ScoreAndFeedback
    suggestions: list[str]


class EssayResponse(EssayAIFeedback):
    overallScore: float
