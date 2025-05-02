from collections import Counter
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ct = Counter(nums)
        for num in nums:
            if ct[num] == 1:
                return num

        