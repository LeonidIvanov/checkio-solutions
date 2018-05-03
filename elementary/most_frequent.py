def most_frequent(data):
    """You have a sequence of strings,
    and you’d like to determine the most frequently occurring string in the sequence.

    Input: a list of strings.

    Output: a string.
    """
    return max(data, key=data.count)


if __name__ == '__main__':

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert most_frequent([
        'a', 'b', 'c',
        'a', 'b',
        'a'
    ]) == 'a'
    assert most_frequent(['a', 'a', 'bi', 'bi', 'bi']) == 'bi'
