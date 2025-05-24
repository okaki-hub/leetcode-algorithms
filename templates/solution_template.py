"""
Problem: Two Sum
Link: https://leetcode.com/problems/two-sum/
KeyWords: Array
Runtime: 0ms
Memory: 13.14MB
Approach:
1. seenリストを使って差分を管理
2. 各要素について、target-numが存在する確認
"""

def towSum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in seen:
            return [seen[diff], i]
        seen[num] = i