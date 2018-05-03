def digits_multiplication(number):
    """You are given a positive integer. Your function should calculate the product of the digits excluding any zeroes.

    For example: The number given is 123405. The result will be 1*2*3*4*5=120 (don't forget to exclude zeroes).

    Input: A positive integer.

    Output: The product of the digits as an integer.

    Precondition: 0 < number < 106
    """
    x = 1
    for n in str(number):
        if n != '0':
            x *= int(n)
    return x


if __name__ == '__main__':

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert digits_multiplication(123405) == 120
    assert digits_multiplication(999) == 729
    assert digits_multiplication(1000) == 1
    assert digits_multiplication(1111) == 1
