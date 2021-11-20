PAIRS = (('(', ')'), ('[', ']'), ('{', '}'))

def is_paired(input_string):
    if not input_string:
        return True
    # Get all kinds of brackets in input_string
    input_brackets = [i for i in input_string if i in '([{}])']
    # Odd length means the brackets are not in pairs
    if len(input_brackets) % 2 != 0:
        return False
    # If the last bracket is an open one, return False
    if input_brackets[len(input_brackets) - 1] in '([{':
        return False    
    half = len(input_brackets) // 2
    i = 0
    while i < half:
        for pair in PAIRS:
            if input_brackets[i] == pair[0] and input_brackets[(len(input_brackets) - 1) - i] != pair[1]:
                if input_brackets[i+1] ==  pair[1]:
                    i += 2
                    continue
                return False 
        i += 1
    return True
