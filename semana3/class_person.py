#person
#dni: int
#name: str
#lastname: int
#role: int

class Person:
    def __init__ (self, dni:int, name:str, lastname:str, role:int):
        self.dni = dni
        self.name = name
        self.lastname = lastname
        self.role = role

    def __repr__ (self):
        return f"name= {self.name, self.lastname}"

person1 = Person (dni = 123, name = "luisito", lastname = "velez", role = 1)
person2 = Person (dni = 456, name = "luis", lastname = "fernandez", role = 2)
person3 = Person (dni = 789, name = "david", lastname = "villa", role = 3)

print (person1)
print (person2)
print (person3)
