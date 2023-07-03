def find(search_list, value):
    if value_in_list(search_list, value):
        return search_list.index(value)
    raise ValueError('value not in array')
        

def value_in_list(lst, value):
    if len(lst) == 0 or (len(lst) == 1 and lst[0] != value):
        return False

    sorted_list = sorted(lst)
    middle = sorted_list[len(sorted_list) // 2]
    if value == middle:
        return True
    elif value < middle:
        return value_in_list(sorted_list[:len(sorted_list) // 2], value)
    else:
        return value_in_list(sorted_list[len(sorted_list) // 2:], value)
