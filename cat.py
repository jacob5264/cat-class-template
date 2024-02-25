#Revmoe pass and complete the cat class
class Cat():
    def __init__(self):
        self.name = "unknown"
        self.age = 0
    
    def speak(self):
        print("meow")

#Create objects here
#These should NOT be indented inside the class

stella = Cat()
stella.name = "stella"
stella.age = 7
speak(stella)

garfield = Cat()
garfield.name = "garfield"
garfield.age = 50
speak(garfield)