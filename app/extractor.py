
import os
from groq import Groq
from dotenv import load_dotenv

from app.tools import PERSON_TOOL, execute_person_tool
from app.exceptions import (
    InvalidInputError,
    ToolExecutionError,
    AIServiceError
)

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("GROQ_API_KEY missing in .env")

client = Groq(api_key=api_key)


def extract_person(text: str):

    if not isinstance(text, str) or not text.strip():
        raise InvalidInputError("Input text cannot be empty")

    try:
        response = client.chat.completions.create(
            model="openai/gpt-oss-120b",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "Extract person details from the text. "
                        "Call submit_person_details with all fields. "
                        "Use null for missing information. "
                        "Never invent details."
                    )
                },
                {"role": "user", "content": text}
            ],
            tools=PERSON_TOOL,
            tool_choice={
                "type": "function",
                "function": {"name": "submit_person_details"}
            }
        )

    except Exception as e:
        raise AIServiceError(
            f"Groq API request failed: {e}"
        ) from e

    try:
        message = response.choices[0].message

        if not message.tool_calls:
            raise ToolExecutionError("AI did not call the required tool")

        tool_call = message.tool_calls[0]

        if tool_call.function.name != "submit_person_details":
            raise ToolExecutionError("Unexpected tool called")

        return execute_person_tool(tool_call.function.arguments)

    except ToolExecutionError:
        raise
    except Exception as e:
        raise AIServiceError(
            f"Failed to process AI response: {e}"
        ) from e
