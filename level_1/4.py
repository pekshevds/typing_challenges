import datetime


def calculate_age(date_of_birth: datetime.date) -> int:
    return datetime.datetime.now().year - date_of_birth.year


if __name__ == "__main__":
    assert calculate_age(date_of_birth=datetime.date(1965, 6, 2)) == 59
