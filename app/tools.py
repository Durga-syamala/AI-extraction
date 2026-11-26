
import json
from pydantic import ValidationError

from app.models import Person
from app.exceptions import ToolExecutionError

PERSON_TOOL = [
    {
        "type": "function",
        "function": {
            "name": "submit_person_details",
            "description": "Submit extracted person information. Use null for missing details.",
            "parameters": {
                "type": "object",
                "properties": {
                    "name": {"type": ["string", "null"]},
                    "age": {"type": ["integer", "null"]},
                    "email": {"type": ["string", "null"]},
                    "profession": {"type": ["string", "null"]},
                    "company": {"type": ["string", "null"]}
                },
                "required": [
                    "name", "age", "email", "profession", "company"
                ],
                "additionalProperties": False
            }
        }
    }
]


def execute_person_tool(arguments: str) -> Person:
    try:
        data = json.loads(arguments)
        return Person.model_validate(data)

    except (json.JSONDecodeError, ValidationError) as e:
        raise ToolExecutionError(
            f"Invalid tool arguments: {e}"
        ) from e
