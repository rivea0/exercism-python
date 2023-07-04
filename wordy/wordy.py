import re
import operator


def answer(question):
    ops = {
        'plus': {
            'op': operator.__add__
        },
        'minus': {
            'op': operator.__sub__
        },
        'multiplied': {
            'op': operator.__mul__
        },
        'divided': {
            'op': operator.__floordiv__
        }
    }

    number_pattern = re.compile('-?\d')
    tokens = re.sub('(\?|What is ?|by)', '', question).split()
    if not tokens: raise ValueError('syntax error')

    if len(tokens) == 1 and number_pattern.match(tokens[0]):
        return int(tokens[0])

    # Raise ValueError if there is no operation
    if not len([t for t in tokens if t in ops]):
        raise ValueError('unknown operation')

    # Raise ValueError if the last token is an operation
    if tokens[len(tokens) - 1] in ops: 
        raise ValueError('syntax error')
    
    result = 0
    prev_tokens = False

    for i, token in enumerate(tokens):
        # Raise ValueError if a number is followed by a number
        if number_pattern.match(token) and i != len(tokens) - 1 and number_pattern.match(tokens[i + 1]):
            raise ValueError('syntax error')
        if token in ops: 
            next_token = tokens[i + 1]
            # Raise ValueError if an operation is followed by an operation
            if next_token in ops:
                raise ValueError('syntax error')
            # Handle single operation
            if not prev_tokens:
                prev_token = tokens[i - 1]
                result += ops[token]['op'](int(prev_token), int(next_token))
                prev_tokens = True
                if [t for t in tokens if t in ops] == 1: return result
            # Handle multiple operations
            else:
                result = ops[token]['op'](result, int(next_token))
    return result
