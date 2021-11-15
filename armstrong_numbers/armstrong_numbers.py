def is_armstrong_number(number):
    num_digits = len(str(number))
    total = sum([int(str(number)[i]) ** num_digits for i in range(num_digits)])
    return number == total
