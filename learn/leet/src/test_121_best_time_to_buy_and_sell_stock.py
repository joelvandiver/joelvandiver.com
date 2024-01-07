from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0
        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)
        return max_profit


def test_wrong_1():
    assert Solution().maxProfit([2, 1, 2, 1, 0, 1, 2]) == 2


def test_1():
    assert Solution().maxProfit([7, 1, 5, 3, 6, 4]) == 5


def test_2():
    assert Solution().maxProfit([7, 6, 4, 3, 1]) == 0


def test_3():
    assert Solution().maxProfit([1, 2]) == 1


def test_4():
    assert Solution().maxProfit([1]) == 0


def test_5():
    assert Solution().maxProfit([1, 2, 3]) == 2


def test_xs():
    assert Solution().maxProfit(list(range(0, 11, 1))) == 10


def test_sm():
    assert Solution().maxProfit(list(range(0, 101, 1))) == 100


def test_md():
    assert Solution().maxProfit(list(range(0, 1001, 1))) == 1000


def test_lg():
    assert Solution().maxProfit(list(range(0, 10001, 1))) == 10000


def test_xl():
    assert Solution().maxProfit(list(range(0, 100001, 1))) == 100000


def test_xxl():
    assert Solution().maxProfit(
        list(range(0, 100001, 1)) + [0]*10000) == 100000


def test_xxxl():
    assert Solution().maxProfit(
        list(range(0, 10000001, 1)) + [0]*1000000) == 10000000
