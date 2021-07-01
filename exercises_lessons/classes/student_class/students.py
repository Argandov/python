#!/usr/bin/python3

"""
1.- Read from file b 
2.- Search in file
3.- Write in file

a) Prep data human > file
b) Prep data file > human

"""


class Students:
    def __init__(self, first, last, courses):
        self.first = first
        self.last = last
        self.courses = courses

    @staticmethod
    def read_file():
        with open('info.txt', 'r') as r:
            student_object = r.readline()
            # name, courses = buff.split(":")[0], \
            #    buff.split(":")[1]
            return student_object

    def check_if_exists(self):
        student = Students(self.first, self.last, self.courses)
        if self == student:
            return True
        else:
            return False

    def __eq__(self):
        pass

    def checker(self):
        print(self)

    def write_file(self):
        with open('info.txt', 'a+') as w:
            w.write(self.first+self.last)
