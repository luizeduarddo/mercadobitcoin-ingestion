
import datetime
import math

class Person:
    def __init__(self, name: str, lastname: str, birth_date: datetime.date):
        self.birth_date = birth_date
        self.lastname = lastname
        self.name = name
    
    @property
    def age(self) -> int:
        return math.floor((datetime.date.today() - self.birth_date).days / 365.2425)

    def __str__(self) -> str:
        return f"{self.name} {self.lastname} has {self.age} years"

luiz = Person(name='Luiz', lastname='Lopes', birth_date=datetime.date(1996, 1, 11))

print(luiz)
print(luiz.age) #Now that function age is a property, dont need () after luiz.age


