
from app.extractor import extract_person
from app.tools import execute_person_tool
from app.exceptions import InvalidInputError, ToolExecutionError


# Test 1: Empty input
try:
    extract_person("")
except InvalidInputError as e:
    print("Empty input handled:", e)


# Test 2: Invalid age
try:
    execute_person_tool(
        '{"name":"Syamala","age":250,"email":null,"profession":null,"company":null}'
    )
except ToolExecutionError as e:
    print("Invalid age handled:", e)


# Test 3: Invalid JSON
try:
    execute_person_tool("invalid json")
except ToolExecutionError as e:
    print("Invalid JSON handled:", e)
