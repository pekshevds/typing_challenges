from constants import ADULT_AGE_BY_COUNTRY


def is_adult(age: int, country_name: str) -> bool:
    adult_age = ADULT_AGE_BY_COUNTRY.get(country_name, 18)
    return age >= adult_age


if __name__ == "__main__":
    assert is_adult(age=17, country_name="Russia") is True
