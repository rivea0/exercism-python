def proverb(*inputs, qualifier=None):
    result = []
    for i, _ in enumerate(inputs):
        if i == 0: first_item = _
        if i == len(inputs) - 1:
            result.append(f'And all for the want of a {qualifier} {first_item}.') if qualifier else result.append(f'And all for the want of a {first_item}.') 
        else:
            items = inputs[i:i + 2]
            result.append(f'For want of a {items[0]} the {items[1]} was lost.')
    return result
