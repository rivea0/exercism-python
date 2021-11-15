class Luhn:
    def __init__(self, card_num):
        self.digits = [int(i) for i in card_num if i.isdigit()]
        self.non_valid_chars = [i for i in card_num if not i.isdigit() and (not i.isspace() or i != ' ')]
          

    def valid(self):
        """Check if a number is valid based on Luhn's algorithm."""
        if self.non_valid_chars:
            return False
        if len(self.digits) <= 1:
            return False
        return sum(self.double_digits()) % 10 == 0
          

    def double_digits(self):
        """Double each second digit, starting from the right."""
        digits_copy = self.digits[:]
        for i in range(len(digits_copy) - 2, -1, -2):
            digits_copy[i] *= 2
            if digits_copy[i] > 9:
                digits_copy[i] -= 9
        return digits_copy
