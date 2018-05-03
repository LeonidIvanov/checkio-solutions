def is_three_words(words):
    """Let's teach the Robots to distinguish words and numbers.

    You are given a string with words and numbers separated by whitespaces (one space). The words contains only letters.
    You should check if the string contains three words in succession.
    For example, the string "start 5 one two three 7 end" contains three words in succession.

    Input: A string with words.

    Output: The answer as a boolean.

    Precondition: The input contains words and/or numbers. There are no mixed words (letters and digits combined).
    0 < len(words) < 100
    """
    i = 0
    for word in words.split():
        if word.isalpha():
            i += 1
        elif word.isdigit() and i < 3:
            i = 0
    if i >= 3:
        return True
    elif i < 3:
        return False
    else:
        return False


if __name__ == '__main__':

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert is_three_words("Hello World hello") == True, "Hello"
    assert is_three_words("He is 123 man") == False, "123 man"
    assert is_three_words("1 2 3 4") == False, "Digits"
    assert is_three_words("bla bla bla bla") == True, "Bla Bla"
    assert is_three_words("Hi") == False, "Hi"
