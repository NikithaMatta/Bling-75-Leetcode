class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        high = nums[n-1] * nums[n-2] * nums[n-3]
        low = nums[n-1] * nums[0] * nums[1]
        return max(high, low)
        