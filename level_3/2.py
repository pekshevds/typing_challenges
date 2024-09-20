from typing import TypedDict


class MyDict(TypedDict):
    name: str
    age: int
    transactions_sums: list[int]


def calculate_total_spent_for_user(user: MyDict) -> int:
    return sum(user.get("transactions_sums", [0]))


if __name__ == "__main__":
    assert (
        calculate_total_spent_for_user(
            user={
                "name": "Ilya",
                "age": 32,
                "transactions_sums": [102, 15, 63, 12],
            },
        )
        == 192
    )
