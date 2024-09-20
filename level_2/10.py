def is_point_in_square(
    point: tuple[int, int],
    left_upper_corner: tuple[int, int],
    right_bottom_corner: tuple[int, int],
) -> bool:
    return (
        left_upper_corner[0] < point[0] < right_bottom_corner[0]
        and left_upper_corner[1] < point[1] < right_bottom_corner[1]
    )


if __name__ == "__main__":
    assert (
        is_point_in_square(
            point=(10, 12), left_upper_corner=(5, 5), right_bottom_corner=(20, 15)
        )
        is True
    )
