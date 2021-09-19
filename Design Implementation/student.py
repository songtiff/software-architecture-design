from person import Person
from enrolled import Enroll

class Student(Person): #student inherits from person 
    def __init__(self, first, last, dob, phone, address, international=False):
        super().__init__(self, first, last, dob, phone, address)
        self.international = international
        self.enrolled = []

    def add_enrollment(self, enroll):
        if not isinstance(enroll, Enroll):
            raise Exception("Invalid Enroll. . . ")

        self.enrolled.append(enroll)

    def is_on_probation(self):
        return False

    def is_part_time(self):
        return len(self.enrolled) <= 3
