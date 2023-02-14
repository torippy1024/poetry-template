from src.main import addition


def test_addition():
    result = addition(2, 3)
    assert result == 5
