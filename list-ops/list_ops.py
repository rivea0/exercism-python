def append(list1, list2):
    return list1 + list2
    

def concat(lists):
    return [item for lst in lists for item in lst]


def filter(function, list):
    return [item for item in list if function(item)]


def length(list):
    return len(list)


def map(function, list):
    return [function(item) for item in list]


def foldl(function, list, initial):
    if not list: return initial
    result = 0
    for item in list:
        result = function(initial, item)
        initial = result
    return result


def foldr(function, list, initial):
    result = foldl(function, reverse(list), initial)
    return result


def reverse(list):
    return list[::-1]

print(foldr(lambda acc, el: el + acc, ["e", "x", "e", "r", "c", "i", "s", "m"], "!"))