import string

def is_pangram(sentence):
    """Check if a sentence uses every letter of the alphabet at least once."""
    for letter in string.ascii_lowercase:
        if letter not in [char.lower() for char in sentence if char.isalpha()]:
            return False
    return True
