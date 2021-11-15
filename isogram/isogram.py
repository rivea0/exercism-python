def is_isogram(string):
    """Check if a word is an isogram ('nonpattern word')."""
    punc = [i for i in string if i == '-' or i == ' ']
    return len(set(string.lower()).difference(set(punc))) == len(string.lower()) - len(punc)
