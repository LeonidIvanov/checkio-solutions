def to_encrypt(text, delta):
    """This mission is the part of the set. Another one - Caesar cipher decriptor.

    Your mission is to encrypt a secret message (text only, without special chars like "!", "&", "?" etc.)
    using Caesar cipher where each letter of input text is replaced by another that stands at a fixed distance.
    For example ("a b c", 3) == "d e f"

    example

    Input: A secret message as a string (lowercase letters only and white spaces)

    Output: The same string, but encrypted

    Precondition:
    0 < len(text) < 50
    -26 < delta < 26
    """
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_text = ''
    for ch in text:
        if ch in alphabet:
            encrypted_ch_index = alphabet.find(ch) + delta
            if encrypted_ch_index > 26:
                encrypted_ch_index -= 26
            encrypted_text += alphabet[encrypted_ch_index]
        else:
            encrypted_text += ch
    return encrypted_text

if __name__ == '__main__':
    print("Example:")
    print(to_encrypt('abc', 10))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert to_encrypt("a b c", 3) == "d e f"
    assert to_encrypt("a b c", -3) == "x y z"
    assert to_encrypt("simple text", 16) == "iycfbu junj"
    assert to_encrypt("important text", 10) == "swzybdkxd dohd"
    assert to_encrypt("state secret", -13) == "fgngr frperg"
    print("Coding complete? Click 'Check' to earn cool rewards!")
