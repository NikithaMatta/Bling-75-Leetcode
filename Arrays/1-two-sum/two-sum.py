class Solution(object):
    def twoSum(self, nums, target):
        map = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in map:
                return [i, map[complement]]
            map[nums[i]] = i
        return []      