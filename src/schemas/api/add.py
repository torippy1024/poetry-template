from pydantic import BaseModel, Field


class ApiAddGetResponse(BaseModel):
    answer: float = Field("", description="Return the sum of a and b")
