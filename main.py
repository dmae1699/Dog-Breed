class Dog:
    animal="dog"
    def __init__(self,breed,colour):
        self.breed=breed
        self.colour=colour
    def display(self):
        print("Breed of dog is", self.breed)
        print("Colour of dog is", self.colour)
d=Dog("rotweiler","black")
d1=Dog("poodle","white and brown")
d.display()
d1.display()
