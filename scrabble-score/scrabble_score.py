LETTER_VALUES = [
    {i: 1 for i in ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T']}, 
    {i: 2 for i in ['D', 'G']}, 
    {i: 3 for i in ['B', 'C', 'M', 'P']},
    {i: 4 for i in ['F', 'H', 'V', 'W', 'Y']},
    {'K': 5},
    {i: 8 for i in ['J', 'X']},
    {i: 10 for i in ['Q', 'Z']}
]


SCRABBLE_LETTERS = {}
for i in LETTER_VALUES:
    SCRABBLE_LETTERS.update(i)


def score(word):
    """Compute the Scrabble score for a given word."""
    total = 0
    for char in word:
        if char.upper() in SCRABBLE_LETTERS:
            total += SCRABBLE_LETTERS[char.upper()]
    return total
