from string import ascii_lowercase, ascii_uppercase


def rotate(text, key):
    lower_table = str.maketrans(ascii_lowercase, ascii_lowercase[key:] + ascii_lowercase[:key])
    upper_table = str.maketrans(ascii_uppercase, ascii_uppercase[key:] + ascii_uppercase[:key])
    return text.translate(lower_table).translate(upper_table)
