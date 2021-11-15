def slices(series, length):
    """Output all the contiguous substrings of length n in given series."""
    if not series:
        raise ValueError('series cannot be empty')
    if length == 0:
        raise ValueError('slice length cannot be zero')
    if length < 0:
        raise ValueError('slice length cannot be negative')
    if length > len(series):
        raise ValueError('slice length cannot be greater than series length')

    slices_ = []
    for i, v in enumerate(series):
        # Check if there is an overflow
        if length > len(series):
            break
        slices_.append(series[i:length])
        length += 1
    return slices_
