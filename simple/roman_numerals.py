def roman_to_arabic(data):
    """Roman numerals come from the ancient Roman numbering system.
    They are based on specific letters of the alphabet which are combined to signify the sum
    (or, in some cases, the difference) of their values.
    The first ten Roman numerals are:

    I, II, III, IV, V, VI, VII, VIII, IX, and X.

    The Roman numeral system is decimal based but not directly positional and does not include a zero.
    Roman numerals are based on combinations of these seven symbols:

    Numeral	Value
    I	1 (unus)
    V	5 (quinque)
    X	10 (decem)
    L	50 (quinquaginta)
    C	100 (centum)
    D	500 (quingenti)
    M	1,000 (mille)
    More additional information about roman numerals can be found on the Wikipedia article.

    For this task, you should return a roman numeral using the specified integer value ranging from 1 to 3999.

    Input: A number as an integer.

    Output: The Roman numeral as a string.

    Precondition: 0 < number < 4000
    """
    ROMANS = (('M', 1000),
              ('CM', 900),
              ('D', 500),
              ('CD', 400),
              ('C', 100),
              ('XC', 90),
              ('L', 50),
              ('XL', 40),
              ('X', 10),
              ('IX', 9),
              ('V', 5),
              ('IV', 4),
              ('I', 1))
    rome_number = ''
    for key, value in ROMANS:
        while data >= value:
            data -= value
            rome_number += key
    return rome_number


if __name__ == '__main__':

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert roman_to_arabic(6) == 'VI', '6'
    assert roman_to_arabic(76) == 'LXXVI', '76'
    assert roman_to_arabic(499) == 'CDXCIX', '499'
    assert roman_to_arabic(3888) == 'MMMDCCCLXXXVIII', '3888'
