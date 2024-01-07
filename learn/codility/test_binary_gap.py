def solution(N: int) -> int:
    '''Find the longest sequence of zeros in the binary representation of an integer.'''
    binary = bin(N)[2:]
    count = 0
    curr = 0
    for i in binary[1:]:
        if i == len(binary) -1:
            break
        if i == '0':
            curr += 1
        else:
            if curr > count:
                count = curr
            curr = 0
    return count


import pytest


@pytest.mark.parametrize(
    "N, expected",
    [
        (0, 0), # 0
        (1, 0), # 1
        (2, 0), # 10
        (3, 0), # 11
        (4, 0), # 100
        (5, 1), # 101
        (6, 0), # 110
        (7, 0), # 111
        (8, 0), # 1000
        (9, 2), # 1001
        (10, 1), # 1010
        (11, 1), # 1011
        (12, 0), # 1100
        (13, 1), # 1101
        (14, 0), # 1110
        (15, 0), # 1111
        (16, 0), # 10000
        (17, 3), # 10001
        (18, 2), # 10010
        (19, 2), # 10011
        (20, 1), # 10100
        (21, 1), # 10101
        (22, 1), # 10110
        (23, 1), # 10111
        (24, 0), # 11000
        (25, 2), # 11001
        (26, 1), # 11010
        (27, 1), # 11011
        (28, 0), # 11100
        (29, 1), # 11101
        (30, 0), # 11110
        (31, 0), # 11111
        (32, 0), # 100000
        (33, 4), # 100001
        (34, 3), # 100010
        (35, 3), # 100011
        (36, 2), # 100100
        (37, 2), # 100101
        (38, 2), # 100110
        (39, 2), # 100111
        (40, 1), # 101000
        (41, 2), # 101001
        (42, 1), # 101010
        (43, 1), # 101011
        (44, 1), # 101100
        (45, 1), # 101101
        (46, 1), # 101110
        (47, 1), #
    ],
)
def test_should_return_the_largest_binary_gap(N, expected):
    assert solution(N) == expected
