def recite(start_verse, end_verse):
    things = [
        'the horse and the hound and the horn',
        'the farmer sowing his corn',
        'the rooster that crowed in the morn',
        'the priest all shaven and shorn', 
        'the man all tattered and torn', 
        'the maiden all forlorn', 
        'the cow with the crumpled horn', 
        'the dog', 
        'the cat', 
        'the rat', 
        'the malt', 
        'the house that Jack built'
    ]

    end = [
        'belonged to',
        'kept',
        'woke',
        'married',
        'kissed',
        'milked',
        'tossed',
        'worried',
        'killed',
        'ate', 
        'lay in'
    ]

    str = f'This is {things[len(things) - end_verse]}'

    for i in range(end_verse - 1):
        str += f' that {end[(len(end) - end_verse) + i + 1]} {things[(len(things) - end_verse) + i + 1]}'
    # for i, v in enumerate(things):
    #     str += f'that {end[end_verse - (i + 1)]} {things[end_verse]} '
    # return f'This is {things[end_verse - 1]} that {end[1]} {things[1]} that {end[0]} {things[0]}.'
    return [f'{str.rstrip()}.']

print(recite(11, 11))