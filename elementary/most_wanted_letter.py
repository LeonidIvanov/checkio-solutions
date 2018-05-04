def get_most_wanted_letter(text):
    """You are given a text, which contains different english letters and punctuation symbols.
    You should find the most frequent letter in the text. The letter returned must be in lower case.
    While checking for the most wanted letter, casing does not matter, so for the purpose of your search, "A" == "a".
    Make sure you do not count punctuation symbols, digits and whitespaces, only letters.

    If you have two or more letters with the same frequency,
    then return the letter which comes first in the latin alphabet.
    For example -- "one" contains "o", "n", "e" only once for each, thus we choose "e".

    Input: A text for analysis as a string.

    Output: The most frequent letter in lower case as a string.

    Precondition:
    A text contains only ASCII symbols.
    0 < len(text) ≤ 105
    """
    ALPH = 'abcdefghijklmnopqrstyvwxyz'
    text = text.lower()
    text = ''.join(sorted(text))
    cleaned_text = [ch for ch in text if ch in ALPH]

    mw_letter, mw_letter_count = cleaned_text[0], cleaned_text.count(cleaned_text[0])
    for ch in cleaned_text[1:]:
        if cleaned_text.count(ch) > mw_letter_count:
            mw_letter, mw_letter_count = ch, cleaned_text.count(ch)
    return mw_letter


if __name__ == '__main__':

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert get_most_wanted_letter("Hello World!") == "l", "Hello test"
    assert get_most_wanted_letter("How do you do?") == "o", "O is most wanted"
    assert get_most_wanted_letter("One") == "e", "All letter only once."
    assert get_most_wanted_letter("Oops!") == "o", "Don't forget about lower case."
    assert get_most_wanted_letter("AAaooo!!!!") == "a", "Only letters."
    assert get_most_wanted_letter("abe") == "a", "The First."
    print("Start the long test")
    assert get_most_wanted_letter("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")
