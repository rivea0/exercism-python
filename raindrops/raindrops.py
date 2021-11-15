def convert(number):
    raindrops = ((3, 'Pling'), (5, 'Plang'), (7, 'Plong'))
    result = [item[1] for item in raindrops if number % item[0] == 0] 
    if result:
        return ''.join(result)
    else:
        return str(number)
