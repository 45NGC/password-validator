def password_validator(password: str) -> bool:
    if len(password) < 6:
        return False

    has_digit = False
    has_upper = False
    has_lower = False
    has_underscore = False

    for character in password:
        if character.isdigit():
            has_digit = True
        elif character.isupper():
            has_upper = True
        elif character.islower():
            has_lower = True
        elif character == '_':
            has_underscore = True

    return has_digit and has_upper and has_lower and has_underscore


if __name__ == "__main__":

    test_passwords = [
        "Abc_12",
        "abc_12",
        "ABC_12",
        "Abc12",
        "A_1b",
    ]

    for password in test_passwords:
        print(f"{password}: {password_validator(password)}")