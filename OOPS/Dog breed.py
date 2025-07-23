class dog:
    animal = "dog"
    def __init__(self, breed, color):
        self.breed = breed
        self.color = color
Dog1 = dog("Alsation", "black-brown")
Dog2 = dog("Golden retreiver", "Golden")
print("Dog1 is a {}".format(Dog1.breed))
print("Dog2 is a {}".format(Dog2.breed))
print("Dog1 is {}".format(Dog1.color))
print("Dog2 is {}".format(Dog2.color))