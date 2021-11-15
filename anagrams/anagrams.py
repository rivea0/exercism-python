from collections import Counter


def find_anagrams(word, candidates):
    count_word = Counter(list(map(ignorecase, word)))
    results = []
    for candidate in candidates:
        count = Counter(list(map(ignorecase, candidate)))
        if count_word == count and word.lower() != candidate.lower():
            results.append(candidate)
    return results
          

def ignorecase(string):
    for i in string:
        return i.lower()
