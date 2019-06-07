import random
class guess:
    def __init__(self):
        self.number=random.randint(10,100)
        print("The random number is",self.number)
        self.user_input()

    def user_input(self):
        self.input=int(input("What's your guess"))
        self.process()

    def process(self):
        if self.input>self.number:
            print("Enter a lower value")
            self.user_input()
        elif self.input<self.number:
            print("Enter a higher number")
            self.user_input()
        else:
            print("Yayy you have guessed the correct number")

obj1=guess()
