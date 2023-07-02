def recite(start_verse, end_verse):
    verses = {
        2: 'the malt that lay',
        3: 'the rat that ate',
        4: 'the cat that killed',
        5: 'the dog that worried',
        6: 'the cow with the crumpled horn that tossed',
        7: 'the maiden all forlorn that milked',
        8: 'the man all tattered and torn that kissed',
        9: 'the priest all shaven and shorn that married',
        10: 'the rooster that crowed in the morn that woke',
        11: 'the farmer sowing his corn that kept',
        12: 'the horse and the hound and the horn that belonged to'
    }

    result = []
    while start_verse <= end_verse:
        build_str = ''
        for i in range(start_verse, 1, -1):
            build_str += f'{verses[i]} '
        result.append(f'This is {f"{build_str}in " if start_verse in verses and end_verse in verses else ""}the house that Jack built.')
        start_verse += 1
    return result
