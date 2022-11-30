import operator

ops = {
    'plus': {
        'priority': False,
        'op': operator.__add__
    },
    'minus': {
        'priority': False,
        'op': operator.__sub__
    },
    'multiplied': {
        'priority': True,
        'op': operator.__mul__
    },
    'divided': {
        'priority': True,
        'op': operator.__floordiv__
    }
}


def trav(lst):
    if len(lst) == 3:
      return ops[lst[1]]['op'](int(lst[0]), int(lst[2]))
    for i in lst:
        if i in ops and ops[i]['priority']:
            result = ops[i]['op'](int(lst[lst.index(i) - 1]), int(lst[lst.index(i) + 1]))
            lst[lst.index(i) - 1:lst.index(i) + 2] = [result]
            return trav(lst)
        elif i in ops:
            result = ops[i]['op'](int(lst[lst.index(i) - 1]), int(lst[lst.index(i) + 1]))
            lst[lst.index(i) - 1:lst.index(i) + 2] = [result]
            return trav(lst)


def is_valid_num(s):
    """Check if the given string is a valid number.
    
    Note: isdigit() and isnumeric() do not work for negative numbers.
    So, we need a custom function.
    """
    try:
        s = int(s)
    except ValueError:
        return False
    return True 


def answer(question):
    parsed = [word for word in question.split() if is_valid_num(word) or word in ops]
    last_word = question.split()[-1][:-1]

    # Add the last word only if it's a number
    parsed.append(last_word if is_valid_num(last_word) else None) 

    if len(parsed) == 1:
        return int(parsed[0])

    return trav(parsed)


