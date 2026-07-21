# Student Class (Encapsulation + OOP)
class Student:
    def __init__(self, student_id, name, course, year_level, gender, email):
        self.student_id = student_id
        self.name = name
        self.course = course
        self.year_level = year_level
        self.gender = gender
        self.__email = email  # Private Attribute (Encapsulation)

    # Getter Method
    def get_email(self):
        return self.__email

    # Setter Method
    def set_email(self, email):
        if email:
            self.__email = email

    def to_tuple(self):
        return (self.student_id, self.name, self.course,
                self.year_level, self.gender, self.__email)

    def display_info(self):
        print("\n--- Student Information ---")
        print(f"Student ID  : {self.student_id}")
        print(f"Name        : {self.name}")
        print(f"Course      : {self.course}")
        print(f"Year Level  : {self.year_level}")
        print(f"Gender      : {self.gender}")
        print(f"Email       : {self.get_email()}")