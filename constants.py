___ = None
USER_BANNED_LIST: list[int] = [3, 5, 7, 13, 8, 32]
ADULT_AGE_BY_COUNTRY: dict[str, int] = {}
with open("level_1/adult_ages_by_countries.txt", mode="r") as file:
    for line in file.readlines():
        key, value = line.split("\t")
        ADULT_AGE_BY_COUNTRY[key] = int(value)
