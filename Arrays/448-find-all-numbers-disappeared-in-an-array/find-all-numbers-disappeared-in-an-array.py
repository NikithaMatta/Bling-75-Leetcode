class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n= []
        new= set(nums)
        for i in range(len(nums)):
            if i+1 not in new:
                n.append(i+1)
        return n
