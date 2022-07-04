import main


def test_to_str_7():
    assert main.to_str('1234567') == '1234567'


def test_to_str_13():
    assert main.to_str('1234567890123') == '1234567890123'


def test_to_str_14():
    assert main.to_str('12345678901234') == '1234567890...'


def test_to_str_0():
    assert main.to_str('') == ''


def test_to_str_7_7():
    assert main.to_str('1234567', 7) == '1234567'


def test_to_str_8_7():
    assert main.to_str('12345678', 7) == '1234...'


