"""
class Dog: 


    def __init__(self,name): #allows to instanciate the object 
        self.name = name # Create an attribute of the class Dog wichs is the Name

    # method is a functions created inside of a Class
    def bark(self): # 
        print("bark")

#d = Dog() # instance of my Class Dog

d = Dog("Tim") # Instance of my class Dog WITH A NAME 

#d.bark() # calling the method of the object


""" 

class student(): 

    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_grade(self):
        return self.grade

    

class course():
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = [] 
    
    def set_maxS(self, max_students):
        self.max_students = max_students

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False

    def get_avg(self):
        value = 0  
        for student in self.students : 
            value += student.get_grade()
        avg =  value / len(self.students) 
        return avg

s1 = student("Camilo", 27 , 100)
s2 = student("Lili" , 29 , 200 )

c1= course("AI", 1) 

c1.add_student(s1)

c1.set_maxS(2)
c1.add_student(s2)

for student in c1.students: 
    print(student.name)

print(c1.get_avg())


