from typing import Any


def is_correct_int(raw_int: Any) -> bool:
    if isinstance(raw_int, int):
        return True
    try:
        int(raw_int)
    except ValueError:
        return False
    except TypeError:
        return False
    return True


if __name__ == "__main__":
    assert is_correct_int(raw_int="12") is True
    assert is_correct_int(raw_int="12&") is False
    assert is_correct_int(raw_int=None) is False
