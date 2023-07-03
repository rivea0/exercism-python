from collections import Counter
import string

def count_words(sentence):
    """Count the occurrences of each word in a given phrase."""
    s = ""
    for i, v in enumerate(sentence):
        if v == "," or v.isspace() or v == "_":   
            s += ' '
        elif v == "'" and i != len(sentence) - 1 and sentence[i+1].isalnum() and sentence[i-1].isalnum():
            s += v
        elif v not in string.punctuation:
            s += v.lower()
    return Counter([i for i in s.split()])
