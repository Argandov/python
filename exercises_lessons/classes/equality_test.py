#!/usr/bin/python3

'''
Evaluando Class objects con __eq__

tester1() y tester2() hacen lo mismo; un class object con "abc", y evaluamos
estos objetos para ver como funciona __eq__

'''

class Tester:

    def __init__(self, string):
        self.string = string

    # __eq__ Hace que 2 CLass Objects se puedan comparar;
    # si quito __eq__, entonces tester evalua a False

    @staticmethod
    def tester():
        string1 = "abc"
        string2 = "abc"
        return Tester(string1) == Tester(string2)

    def tester2(self):
        string3 = "abc"
        return Tester(string3) == self
        # Donde self -> Tester('abc')

    def __eq__(self, other):
        return self.string == other.string


print(Tester("abc").tester())
print(Tester("abc").tester2())
# solo corroborando los metodos que tiene el Class Object
print(dir(Tester))
