def factors(value):
    """Compute the prime factors of a given number."""
    results = []
    while value != 1:
        for i in range(2, value+1):
            if value % i == 0:
                results.append(i)
                value //= i
                break
    return results
