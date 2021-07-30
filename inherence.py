class pet:
    def __init__(self, name,age):
        self.name =name 
        self.age = age
    def say(self):
        print("idk what to say")

class cat(pet):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color


    def say(self):
        print("I say meow")

class dog(pet):
    def say(self): 
        print("i say bark")


pet = pet("camilo", 27)
pet.say()
dog = dog("aker", 7)
dog.say()
cat = cat("ronaldo", 1, "green")
cat.say()
print(cat.color)