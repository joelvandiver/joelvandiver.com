from typing import List

# https://leetcode.com/problems/merge-sorted-array/


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        result = []
        while m > 0 or n > 0:
            if n == 0:
                result.append(nums1.pop(0))
                m -= 1
            elif m == 0:
                result.append(nums2.pop(0))
                n -= 1
            elif nums1[0] <= nums2[0]:
                result.append(nums1.pop(0))
                m -= 1
            else:
                result.append(nums2.pop(0))
                n -= 1
        nums1[:] = result


def test_merge_1():
    solution = Solution()
    nums1 = [1, 2, 3, 0, 0, 0]
    solution.merge(nums1, 3, [2, 5, 6], 3)
    assert nums1 == [1, 2, 2, 3, 5, 6]


def test_merge_2():
    solution = Solution()
    nums1 = [1]
    solution.merge(nums1, 1, [], 0)
    assert nums1 == [1]


def test_merge_3():
    solution = Solution()
    nums1 = [0]
    solution.merge(nums1, 0, [1], 1)
    assert nums1 == [1]


def test_merge_4():
    solution = Solution()
    nums1 = [4, 0, 0, 0, 0, 0]
    solution.merge(nums1, 1, [1, 2, 3, 5, 6], 5)
    assert nums1 == [1, 2, 3, 4, 5, 6]


def test_merge_5():
    solution = Solution()
    nums1 = [-1, 0, 0, 3, 3, 3, 0, 0, 0]
    solution.merge(nums1, 6, [1, 2, 2], 3)
    assert nums1 == [-1, 0, 0, 1, 2, 2, 3, 3, 3]


def test_merge_6():
    solution = Solution()
    nums1 = [-1, 3, 0, 0, 0, 0, 0]
    solution.merge(nums1, 2, [0, 0, 1, 2, 3], 5)
    assert nums1 == [-1, 0, 0, 1, 2, 3, 3]


def test_merge_7():
    solution = Solution()
    nums1 = [-1, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0]
    solution.merge(nums1, 5, [-1, -1, 0, 0, 1, 2], 6)
    assert nums1 == [-1, -1, -1, 0, 0, 0, 0, 0, 1, 2, 3]


def test_merge_8():
    solution = Solution()
    nums1 = [0, 2, 0, 0, 0, 0, 0]
    solution.merge(nums1, 2, [-1, -1, 2, 5, 6], 5)
    assert nums1 == [-1, -1, 0, 2, 2, 5, 6]
