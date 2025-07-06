def password_validator(password: str) -> bool:
    print('x')
    pass


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