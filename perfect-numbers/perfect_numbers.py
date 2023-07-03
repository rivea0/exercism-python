def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number < 1:
        raise ValueError('Classification is only possible for positive integers.')
    factors = [i for i in range(1, number) if number % i == 0]
    return is_perfect(sum(factors), number)


def is_perfect(aliquot_sum, number):
    classifications = (
        (aliquot_sum == number, 'perfect'),
        (aliquot_sum > number, 'abundant'),
        (aliquot_sum < number, 'deficient')
    )
    return [i[1] for i in classifications if i[0]][0]
