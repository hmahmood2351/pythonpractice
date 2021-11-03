#tutorial

class Student:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

John = Student("John", "21")
Jane = Student("Jane", "22")
print(getattr(John, "age"))


#exercises

class StudentNew:

    def __init__(self, name, age, class_='student'):
        self.name = name
        self.age = age
        self.class_ = class_

    def avgtestscore(self, score1, score2, score3):
        print("Average test score is: ", ((score1+score2+score3))/3)

bob = StudentNew("bob", 21)
bob.avgtestscore(100, 100, 100)
print(getattr(bob, "class_"))
