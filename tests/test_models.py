
from app.models import Person

person = Person(
    name="syamala",
    age=25,
    email="syamala@gmail.com",
    profession="Developer",
    company="ABC Tech"
)

print(person)
print(person.model_dump())
