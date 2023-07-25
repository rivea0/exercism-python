def prime(number):
    if number < 1:
        raise ValueError('there is no zeroth prime')
    primes = [2]
    n = 2
    while len(primes) < number:
        while True:
            n += 1
            if all(n % p != 0 for p in primes):
                primes.append(n)
                break
    return primes[-1]
