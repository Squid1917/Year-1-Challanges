class Student():
    def __init__(self,ID,Name,Class,Grade):
        self.ID = ID
        self.Name = Name
        self.Class = Class
        self.Grade = Grade

Student1 = Student(0,"Seth","Mark","B")
Student2 = Student(1,"Lewis","Mark","F")

print(Student2.__dict__)

Student1.__delattr__("Grade")
print(Student1.__dict__)

