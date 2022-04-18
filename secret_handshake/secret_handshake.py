def commands(binary_str):
    result = []
    mapping = {
        0: '',
        1: 'wink',
        10: 'double blink',
        100: 'close your eyes',
        1000: 'jump',
    }

    for i in range(len(binary_str)):
        if binary_str == 0 * len(binary_str):
            break
        # Get the value of the binary digit
        n = int(binary_str[-(i + 1)]) * (10 ** i)
        if n == 10000:
            result = list(reversed(result))
        else:                          
            result.append(mapping[n])
        # Replace the handled value with 0
        binary_str = binary_str[:-(i + 1)] + ('0' * (i + 1))

    return [handshake for handshake in result if handshake]
