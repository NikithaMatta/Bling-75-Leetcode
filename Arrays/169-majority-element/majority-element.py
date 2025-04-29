from collections import Counter

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ct = Counter(nums)
        n = len(nums)
        for num in nums:
            if ct[num] > n/2:
                return num
        