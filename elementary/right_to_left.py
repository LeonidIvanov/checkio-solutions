def left_join(phrases):
    """One of the robots is charged with a simple task:
        to join a sequence of strings into one sentence to produce instructions on how to get around the ship.
    But this robot is left-handed and has a tendency to joke around and confuse its right-handed friends.

    You are given a sequence of strings.
    You should join these strings into chunk of text where the initial strings are separated by commas.
    As a joke on the right handed robots, you should replace all cases of the words "right" with the word "left",
    even if it's a part of another word. All strings are given in lowercase.

    Input: A sequence of strings as a tuple of strings (unicode).

    Output: The text as a string.

    Precondition:
    0 < len(phrases) < 42
    """
    phrase = ''
    for s in phrases:
        if s is not phrases[-1]:
            phrase += s + ','
        else:
            phrase += s
    phrase = phrase.replace('right', 'left')
    return phrase


if __name__ == '__main__':

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert left_join(("left", "right", "left", "stop")) == "left,left,left,stop", "All to left"
    assert left_join(("bright aright", "ok")) == "bleft aleft,ok", "Bright Left"
    assert left_join(("brightness wright",)) == "bleftness wleft", "One phrase"
    assert left_join(("enough", "jokes")) == "enough,jokes", "Nothing to replace"
