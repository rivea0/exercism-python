def sum_of_multiples(limit, multiples):
    return sum({i for i in range(1, limit) for j in multiples if j != 0 and i % j == 0})
