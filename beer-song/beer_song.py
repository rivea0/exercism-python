def recite(start, take=1):
    if take == 0:
        line_break = False
        return []
    if take == 1:
        line_break = False
    else:
        line_break = True
    
    # The first and the second lines for default numbers
    first_line = f'{start} bottles of beer on the wall, {start} bottles of beer.'
    second_line = f'Take one down and pass it around, {start - 1} bottles of beer on the wall.'

    # All the cases for minor differences for numbers 2, 1, and 0
    if start == 2:
        first_line = f'{start} bottles of beer on the wall, {start} bottles of beer.'
        second_line = f'Take one down and pass it around, {start - 1} bottle of beer on the wall.'

    if start == 1:
        first_line = f'{start} bottle of beer on the wall, {start} bottle of beer.'
        second_line = 'Take it down and pass it around, no more bottles of beer on the wall.'

    if start == 0:
        first_line = 'No more bottles of beer on the wall, no more bottles of beer.'
        second_line = 'Go to the store and buy some more, 99 bottles of beer on the wall.'

    result = []
    if not line_break:
        result.extend([first_line, second_line])
    else:
        result.extend([first_line, second_line, ''])
    result.extend(recite(start - 1, take - 1)) 
    return result 
