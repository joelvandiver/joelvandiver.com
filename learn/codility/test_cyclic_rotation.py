def solution(A: list[int], K: int) -> list[int]:
    l = len(A)
    if l == 0:
        return []
    result = [None for i in range(l)]
    k = K % l
    for i in range(l - 1, -1, -1):
        v = A[i]
        if i + k < l:
            x = i + k
        else:
            x = k + i - l
        result[x] = v
    return result


import pytest


@pytest.mark.parametrize(
    "A, k, s",
    [
        ([], 1, []),
        ([0, 1], 1, [1, 0]),
        ([3, 8, 9, 7, 6], 3, [9, 7, 6, 3, 8]),
        ([1, 2, 3], 10, [3, 1, 2])
    ],
)
def test_should_return_the_expected_value(
    A: list[int], k: int, s: list[int]
):
    assert solution(A, k) == s
