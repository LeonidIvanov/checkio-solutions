def get_safe_pawns(pawns):
    """A pawn is generally a weak unit, but we have 8 of them which we can use to build a pawn defense wall.
    With this strategy, one pawn defends the others. A pawn is safe if another pawn can capture a unit on that square.
    We have several white pawns on the chess board and only white pawns.
    You should design your code to find how many pawns are safe.

    You are given a set of square coordinates where we have placed white pawns.
    You should count how many pawns are safe.

    Input: Placed pawns coordinates as a set of strings.

    Output: The number of safe pawns as a integer.

    Precondition:
    0 < pawns ≤ 8
    """
    rows = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
    safe_pawns = 0
    y = [[int(pawn[1]) - 1, rows[pawn[0]]] for pawn in pawns]
    y.sort(reverse=True)
    for i in range(len(y)):
        i -= safe_pawns
        if [y[i][0] - 1, y[i][1] - 1] in y or [y[i][0] - 1, y[i][1] + 1] in y:
            safe_pawns += 1
            del y[i]
    return safe_pawns


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert get_safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert get_safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
