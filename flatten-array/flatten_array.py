def flatten(iterable):
    flat = []
    for i in iterable:
        if type(i) == list:
            flat += flatten(i)
        elif i != None: # Just checking for i ignores 0 values
            flat.append(i)
    return flat 
