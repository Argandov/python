#!/usr/bin/python3

class Students:

    # None es un default(opcional): en caso de que invoquemos el método sin argumentos, la instancia se rellena con None
    # Self es sólo una convención. Yuck es cualquier otro nombre para "self"
    def __init__(yuck,first=None,last=None,courses=None):
        yuck.first_name = first
        yuck.last_name = last
        yuck.courses = courses
    
    # No es necesario llamar a self/yuck, si la variable es local a la instancia:
    def subscribe(self,course):
        print(f"{self.first_name} is succesfully \
subscribed to: {course}")
    
    def __str__(self):
        return f"Default string. Your student name is {self.first_name} {self.last_name}"

    def __repr__(self):
        return f"Name: {self.first_name}"

    def __hash__(self):
        return hash(self.first_name)

john_profile = ["python","c"]
josh_profile = ["java","lua"]

john = Students("john","wick",john_profile)
josh = Students("josh","werkzeug")

print(john.first_name)
print(josh.courses)

john.subscribe("data structures")
# __str__ method (string representation)
print(john)

# Object Methods
print(dir(john))        # Métodos del objeto
print(john.__dict__)    # dict del objeto john

# Special Methods (Inside the Students class):
print(repr(john))       # porque __str__ ya existe, llamamos __repr__
print(hash(john))


# __repr__ uso:
class Cars:
    def __init__(self, brand):
        self.brand = brand

    def __repr__(self):
        return f"Car's brand is {self.brand}"

print(Cars("audi"))
