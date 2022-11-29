from datetime import timedelta

def add(moment):
    gigasecond = 10 ** 9
    return moment + timedelta(seconds=gigasecond)
