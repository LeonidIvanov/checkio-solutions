def best_stock(data):
    """You are given the current stock prices. You have to find out which stocks cost more.

    Input: The dictionary where the market identifier code is a key and the value is a stock price.

    Output: A string and the market identifier code.

    Preconditions: All the prices are unique.
    """
    return max(data, key=data.get)


if __name__ == '__main__':

    # These "asserts" are used for self-checking and not for an auto-testing
    assert best_stock({
        'CAC': 10.0,
        'ATX': 390.2,
        'WIG': 1.2
    }) == 'ATX', "First"
    assert best_stock({
        'CAC': 91.1,
        'ATX': 1.01,
        'TASI': 120.9
    }) == 'TASI', "Second"
