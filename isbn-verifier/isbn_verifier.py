import string

def is_valid(isbn):
    if not isbn:
        return False 
    letters = [x for x in isbn if x in string.ascii_letters and x != 'X']
    if letters:
        return False
    digits = []
    for i in isbn:
        if i.isdigit():
            digits.append(int(i))
        elif i == 'X' and isbn.index(i) == len(isbn) - 1:
            digits.append(10)
    if len(digits) != 10:
        return False
    return check_total(digits) % 11 == 0


def check_total(digits):
    total = 0
    i = 10
    j = i
    while i > 0:
        total += i * digits[j-i]
        i -= 1
    return total 
