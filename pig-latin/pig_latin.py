def translate(text):
    return ' '.join([pig_latin(word) for word in text.split()])


def is_vowel(letter):
    return letter in ('a', 'e', 'i', 'o', 'u')


def pig_latin(word):
    if is_vowel(word[0]) or word[:2] == 'xr' or word[:2] == 'yt' or (word[0] == 'y' and not is_vowel(word[1])):
         return f'{word}ay'
    if word[:2] == 'qu':
        return pig_latin(f'{word[2:]}{word[:2]}')
    return pig_latin(f'{word[1:]}{word[0]}')
