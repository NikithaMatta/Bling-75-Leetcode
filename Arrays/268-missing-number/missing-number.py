class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        if len(nums) not in nums:
            return len(nums)
        for i in range(len(nums)):
            if nums[i] != i:
                return i
