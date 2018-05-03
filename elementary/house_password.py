def check_password(data):
    """Stephan and Sophia forget about security and use simple passwords for everything.
    Help Nikola develop a password security check module.
    The password will be considered strong enough if its length is greater than or equal to 10 symbols,
    it has at least one digit, as well as containing one uppercase letter and one lowercase letter in it.
    The password contains only ASCII latin letters or digits.

    Input: A password as a string.

    Output: Is the password safe or not as a boolean or any data type that can be converted and processed as a boolean.
    In the results you will see the converted results.

    Precondition:
    re.match("[a-zA-Z0-9]+", password)
    0 < len(password) ≤ 64
    """
    nums = ''.join(str(i) for i in range(10))
    low_letter = 'abcdefghijklmnopqrstuvwxyz'
    up_letter = low_letter.upper()

    num_count = 0
    up_letter_count = 0
    low_letter_count = 0

    if len(data) < 10:
        print('Password must be 10 symbols at least')
        return False
    else:
        for ch in data:
            if ch in nums:
                num_count += 1
            elif ch in up_letter:
                up_letter_count += 1
            elif ch in low_letter:
                low_letter_count += 1
        if num_count > 0 and up_letter_count > 0 and low_letter_count > 0:
            return True
        else:
            return False


if __name__ == '__main__':

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert check_password('A1213pokl') == False, "1st example"
    assert check_password('bAse730onE4') == True, "2nd example"
    assert check_password('asasasasasasasaas') == False, "3rd example"
    assert check_password('QWERTYqwerty') == False, "4th example"
    assert check_password('123456123456') == False, "5th example"
    assert check_password('QwErTy911poqqqq') == True, "6th example"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
