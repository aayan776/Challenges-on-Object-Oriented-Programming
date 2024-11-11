import random
class Op_overload:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Op_overload(x, y)
obj1 = Op_overload(1,2)
obj2 = Op_overload(10,5)
print(obj1 + obj2)
class fruit_quiz:
    def __init__(self):
        self.fruits = {"Orange" : "orange", "Apple" : "red", "Papaya" : "orange", "Mango" : "yellow", "Watermelon" : "green", "Banana" : "yellow"}
    def quiz(self):
        while (True):
            fruit, color = random.choice(list(self.fruits.items()))
            print("What color is {}".format(fruit))
            ans = input("Enter colour name: ").lower()
            if ans == color:
                print("Correct!")
            else:
                print("Wrong!")
            option = int(input("Enter 0 if you want to play again. Otherwise enter 1: "))
            if option:
                break
print("Welcome to the esteemed quiz of fruits")
obj3 = fruit_quiz()
obj3.quiz()