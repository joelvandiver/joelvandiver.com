# https://leetcode.com/problems/running-sum-of-1d-array/
from typing import List

# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

# Return the running sum of nums.

# Constraints:

# 1 <= nums.length <= 1000
# -10^6 <= nums[i] <= 10^6


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        # sum = 0
        # return [
        #     sum := sum + num
        #     for num in nums]
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
        return nums


def test_should_solve_example_1():
    # Example 1:

    # Input: nums = [1,2,3,4]
    # Output: [1,3,6,10]
    # Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
    input = [1, 2, 3, 4]
    assert [1, 3, 6, 10] == Solution().runningSum(input)


def test_should_solve_example_2():
    # Example 2:

    # Input: nums = [1,1,1,1,1]
    # Output: [1,2,3,4,5]
    # Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].
    input = [1, 1, 1, 1, 1]
    assert [1, 2, 3, 4, 5] == Solution().runningSum(input)


def test_should_solve_example_3():
    # Example 3:

    # Input: nums = [3,1,2,10,1]
    # Output: [3,4,6,16,17]
    input = [3, 1, 2, 10, 1]
    assert [3, 4, 6, 16, 17] == Solution().runningSum(input)
