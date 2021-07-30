class person: 
    
    number_of_people= 0

    def __init__(self, name):
        self.name = name
        person.add_person()


    ## I dont need instance to call this methods
    @classmethod
    def numberOfPeople(cls):
        return cls.number_of_people

    @classmethod
    def add_person(cls):
        cls.number_of_people += 1

p1 = person("Camilo")
print(person.number_of_people)
p2 = person("Laura")
print(person.number_of_people)
person.add_person()
print(person.number_of_people)