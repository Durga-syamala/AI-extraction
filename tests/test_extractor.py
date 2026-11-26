from app.extractor import extract_person

text = """
My name is Syamala.
I am 25 years old.
My email is syamala@gmail.com.
I work as a Python Developer at ABC Tech.
"""

person = extract_person(text)

print("Extracted Person:")
print(person.model_dump())