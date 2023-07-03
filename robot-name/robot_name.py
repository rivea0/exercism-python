import random 

from string import digits, ascii_uppercase as au


class Robot:
    def __init__(self):
        self.name = self.generate_name()


    def generate_name(self):
        random.seed()
        self.letters = [random.choice(au) for i in range(2)]
        self.r_digits = [str(random.randint(int(digits[0]), int(digits[-1]))) for i in range(3)]
        self.name = "".join(self.letters) + "".join(self.r_digits)
        return self.name 


    def reset(self):
        return self.generate_name()
