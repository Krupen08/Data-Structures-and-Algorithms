# Two Sum

## Problem

Given an array of integers `nums` and an integer `target`, return the indices of the two numbers such that they add up to `target`.

## Approach

Use two nested loops to check every possible pair of numbers.

## Complexity

- Time Complexity: O(n²)
- Space Complexity: O(1)

## Solution

```python
class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
```
