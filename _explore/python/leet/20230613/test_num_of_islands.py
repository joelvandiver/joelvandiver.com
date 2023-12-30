from typing import List


class Solution:
    """
    Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

    An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
    """
    def numIslands(self, grid: List[List[str]]) -> int:
        for row in grid:
            for col in row:
                print(col)
        return 0


def test_should_solve_simple_1():
    input = [
        ["1", "1" ],
        ["0", "0" ]
    ]
    assert 1 == Solution().numIslands(input)

def test_should_solve_example_1():
    input = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]
    assert 1 == Solution().numIslands(input)
