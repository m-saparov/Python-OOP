
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def show_info(self):
        print(f"{self.name} - {self.age} yoshda")
        

s1 = Student("student-1", 12)
s2 = Student("student-2", 16)
s3 = Student("student-3", 20)
s4 = Student("student-4", 18)
s5 = Student("student-5", 10)

students = [s1, s2, s3, s4, s5]

max_s = max(students, key=lambda s: s.age)
max_s.show_info()