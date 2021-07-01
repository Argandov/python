# Upon completing the prep_record and prep_to_write functions
# we are ready to add them to the Student class. Note: The completed
# functions are in the read_and_write_demo.py file also attached
# to this video

# We added the find_in_file and add_to_file methods to the class below.
# We added in the prep_record function as a static method because while
# it is associated with the class, it isn't directly tied to either the
# class or any instance of student objects

# We also utilized the special __eq__() method to provide our own
# definition of what an equality test of different objects of the class
# should look like

class Student:

    def __init__(self, first, last, courses=None):
        self.first_name = first
        self.last_name = last
        if courses == None:
            self.courses = []
        else:
            self.courses = courses

    def add_course(self, course):
        if course not in self.courses:
            self.courses.append(course)
        else:
            print(f"{self.first_name} is already \
                enrolled in the {course} course")

    def remove_course(self, course):
        if course in self.courses:
            self.courses.remove(course)
        else:
            print(f"{course} not found")

    def find_in_file(self, filename):
        with open(filename) as f:
            for line in f:
                first_name, last_name, course_details = Student.prep_record(line.strip())
                student_read_in = Student(first_name, last_name, course_details)
                if self == student_read_in:
                    return True
            return False

    def add_to_file(self, filename):
        pass

    @staticmethod
    def prep_record(line):
        line = line.split(":")
        first_name, last_name = line[0].split(",")
        course_details = line[1].rstrip().split(",")
        return first_name, last_name, course_details

    def __eq__(self, other):
        return self.first_name == other.first_name \
        and self.last_name == other.last_name

    def __len__(self):
        return len(self.courses)

    def __repr__(self):
        return f"Student('{self.first_name}','{self.last_name}',{self.courses})"

    def __str__(self):
        return f"First name: {self.first_name.capitalize()}\nLast name: {self.last_name.capitalize()}\
        \nCourses: {', '.join(map(str.capitalize, self.courses))}"

file_name = 'data.txt'
courses = ["c","ruby","javascript"]
jane = Student("jane","doe",courses)
print(dir(Student))
# Write some execution code to see if this student object exists
# in the data.txt file (file_name variable above). If it doesn't exist
# in the file you can add this record to the file to test this
# find_in_file functionality jane,doe:c,ruby,javascript
