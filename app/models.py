
from pydantic import BaseModel, ConfigDict, EmailStr, Field, field_validator


class Person(BaseModel):
    model_config = ConfigDict(extra="forbid")

    name: str | None = Field(
        default=None,
        description="Person's full name, or null if not mentioned"
    )

    age: int | None = Field(
        default=None,
        description="Person's age, or null if not mentioned"
    )

    email: EmailStr | None = Field(
        default=None,
        description="Person's email address, or null if not mentioned"
    )

    profession: str | None = Field(
        default=None,
        description="Person's profession, or null if not mentioned"
    )

    company: str | None = Field(
        default=None,
        description="Person's company, or null if not mentioned"
    )

    @field_validator("age")
    @classmethod
    def validate_age(cls, value):
        if value is not None and not 0 <= value <= 120:
            raise ValueError("Age must be between 0 and 120")
        return value


class ExtractionRequest(BaseModel):
    text: str = Field(min_length=1)


class ExtractionResponse(BaseModel):
    success: bool
    data: Person | None = None
    errors: list[str] = Field(default_factory=list)
