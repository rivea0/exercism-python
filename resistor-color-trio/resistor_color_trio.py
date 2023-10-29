COLOR_VALUES = {
    'black': 0,
    'brown': 1,
    'red': 2,
    'orange': 3,
    'yellow': 4,
    'green': 5,
    'blue': 6,
    'violet': 7,
    'grey': 8,
    'white': 9,        
}

METRIC_PREFIXES = { 3: 'kilo', 6: 'mega', 9: 'giga' }

def label(colors):
    num_zeroes_to_add = COLOR_VALUES[colors[2]]
    result = int(str(COLOR_VALUES[colors[0]]) + str(COLOR_VALUES[colors[1]])) * 10 ** num_zeroes_to_add
    num_zeroes_total = str(result).count('0')
    prefix = ''
    prefix_int = 1

    for exponent in sorted(METRIC_PREFIXES.keys(), reverse=True):
        if num_zeroes_total >= exponent:
            prefix_int = 10 ** exponent
            prefix = METRIC_PREFIXES[exponent]
            break

    return f'{result // prefix_int} {prefix}ohms'
