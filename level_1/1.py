import constants


def is_user_banned(user_id: int) -> bool:
    return user_id in constants.USER_BANNED_LIST


if __name__ == "__main__":
    assert is_user_banned(user_id=32) is True
    assert is_user_banned(user_id=2) is False
