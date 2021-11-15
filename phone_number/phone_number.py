import string
          

class PhoneNumber:
    def __init__(self, number):
        letters = [i for i in number if i in string.ascii_letters]
        if letters:
            raise ValueError('letters not permitted')
        allowed = ['(', ')', '-', ' ', '.', '+']
        punc = [i for i in number if i in string.punctuation and i not in allowed]
        if punc:
            raise ValueError('punctuations not permitted')
        self.number = ''.join([i for i in number if i.isdigit()])
        self.clean()
        self.area_code = self.number[:3]
        self.exchange_code = self.number[3:6]
        self.subscriber_num = self.number[6:]
        self.check()
          

    def clean(self):
        if len(self.number) > 10 and self.number[0] == '1':
            self.number = self.number[1:]


    def check(self):
        if len(self.number) < 10:
            raise ValueError("incorrect number of digits")
        if len(self.number) > 11:
            raise ValueError("more than 11 digits")
        if len(self.number) == 11 and self.number[0] != 1:
            raise ValueError("11 digits must start with 1")
        if self.exchange_code[0] == '0':
            raise ValueError("exchange code cannot start with zero")
        if self.exchange_code[0] == '1':
            raise ValueError("exchange code cannot start with one")
        if self.area_code[0] == '0':
            raise ValueError("area code cannot start with zero")
        if self.area_code[0] == '1':
            raise ValueError("area code cannot start with one")	


    def pretty(self):
        return '(' + self.area_code + ')' + '-' + self.exchange_code + '-' + self.subscriber_num
