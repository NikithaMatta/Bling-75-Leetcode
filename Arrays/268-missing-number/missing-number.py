class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s1 = sum(range(len(nums)+1))
        s2 = sum(nums)
        return s1-s2