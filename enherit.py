class Animal:
    def __init__(self,  name):
        self.name = name
    
    def propeties(self):
        print(f"{self.name} is animal haha")
    def check(self):
        print("yes")

class Dog(Animal):
    def sound(self):
        print(f"{self.name} barks")


animal = Animal("cock")
animal.propeties()
dog = Animal("dog")
dog.propeties()
dog = Dog("dog")
dog.sound()
dog.check()