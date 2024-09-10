from typing import Any


def stringify(value: Any) -> str:
    return str(value)


if __name__ == "__main__":
    assert stringify(value="12") == "12"
    assert stringify(value=15) == "15"
    assert stringify(value=0.5) == "0.5"
    assert stringify(value=None) == "None"
