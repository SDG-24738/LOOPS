class supervillain:
    def __init__(self, name, goal):
        self.name = name
        self.goal = goal
    def catchphrase(self):
        print(f"{self.name} says I am inveitable")
Villain1 = supervillain("Thanos", "Universal genocide")
villain2 = supervillain("Docter Doom", "Multiversal domination")
print(f"Marvel's old villain was {Villain1.name} and his goal was to {Villain1.goal}. ")
print(f"Marvel's new villain is {villain2.name} and his goal is to {villain2.goal}. ")
