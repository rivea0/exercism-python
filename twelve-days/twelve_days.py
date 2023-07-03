DAYS = ('first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 'ninth', 'tenth', 'eleventh', 'twelfth')

GIFTS = (
    'a Partridge in a Pear Tree', 
    'two Turtle Doves', 
    'three French Hens', 
    'four Calling Birds', 
    'five Gold Rings', 
    'six Geese-a-Laying', 
    'seven Swans-a-Swimming', 
    'eight Maids-a-Milking', 
    'nine Ladies Dancing', 
    'ten Lords-a-Leaping', 
    'eleven Pipers Piping', 
    'twelve Drummers Drumming'
)

song = []
          

def get_song(gifts, day):
    """Get the lyrics to 'The Twelve Days of Christmas'."""
    if len(gifts) == 0:
        return gifts
    if len(gifts) == 1:
        song.append(f'On the {DAYS[day]} day of Christmas my true love gave to me: {gifts[0]}.')
    else:    
        get_song(gifts[:-1], day-1)
        song.append(f'On the {DAYS[day]} day of Christmas my true love gave to me: {", ".join(gifts[:-(len(gifts)):-1])}, and {gifts[0]}.')
    return song


def recite(x, y):
    """Output the lyrics to 'The Twelve Days of Christmas'."""
    total_song = get_song(GIFTS, len(DAYS) - 1)
    return total_song[x-1:y]
