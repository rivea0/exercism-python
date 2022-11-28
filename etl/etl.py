def transform(legacy_data):
    return {letter.lower(): score for score, v in legacy_data.items() for letter in v}

