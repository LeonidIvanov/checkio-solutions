def even_last(array):
    """You are given an array of integers.
    You should find the sum of the elements with even indexes (0th, 2nd, 4th...) then multiply this summed number
    and the final element of the array together. Don't forget that the first element has an index of 0.

    For an empty array, the result will always be 0 (zero).

    Input: A list of integers.

    Output: The number as an integer.

    Precondition: 0 ≤ len(array) ≤ 20
    all(isinstance(x, int) for x in array)
    all(-100 < x < 100 for x in array)
    """
    if array == []:
        return 0
    sum = 0
    for n in array[::2]:
        sum += n
    total = sum * array[-1]
    return total

if __name__ == '__main__':

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert even_last([0, 1, 2, 3, 4, 5]) == 30, "(0+2+4)*5=30"
    assert even_last([1, 3, 5]) == 30, "(1+5)*5=30"
    assert even_last([6]) == 36, "(6)*6=36"
    assert even_last([]) == 0, "An empty array = 0"
