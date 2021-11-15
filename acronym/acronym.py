def check(word, index):
    """Check for acronyms."""
    return not word[index-1].isalpha() and word[index-1] != "'" and word[index].isalpha()
          

def abbreviate(words):
    """Convert a phrase to its acronym."""
    letters = [words[i].upper() for i in range(1, len(words)) if check(words, i)]
    return words[0] + ''.join(letters)
