from password_validator import password_validator

def test_valid_password():
    assert password_validator("Abc_12") == True

def test_too_short():
    assert password_validator("A_1b") == False

def test_missing_uppercase():
    assert password_validator("abc_12") == False

def test_missing_lowercase():
    assert password_validator("ABC_12") == False

def test_missing_digit():
    assert password_validator("Abc_def") == False

def test_missing_underscore():
    assert password_validator("Abc123") == False

def test_all_missing():
    assert password_validator("") == False

def test_edge_case_exact_length():
    assert password_validator("A1_bcd") == True
