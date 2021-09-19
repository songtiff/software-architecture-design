from prof import Professor
from enrolled import Enroll

class Course:
    def __init__(self, name, code, max_, min_, professor):
        self.name = name
        self.code = code
        self.max = max_
        self.min = min_
        self.professors = []
    
        if isinstance(professor, Professor):
                self.professors.append(professor)
        elif isinstance(professor, list):
            for entry in professor:
                if not isinstance(entry, Professor):
                    raise Exception("Invalid professor. . . ")
            
            self.professors = professor
        else:
            raise Exception("Invalid professor. . . ")

    def add_professor(self, professor):
        if not isinstance(professor, Professor):
            raise Exception("Invalid professor. . . ")
        else:
            self.professors.append(professor)

    def add_enrollment(self, enroll):
        if not isinstance(enroll, Enroll):
            raise Exception("Invalid enrollment. . . ")
        
        if len(enroll) == self.max:
            raise Exception("Cannot enroll, course is full")

        self.enrollments.append(enroll)

    def is_cancelled(self):
        return len(self.add_enrollments) < self.min
