class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        # Convert all numbers to strings
        nums = list(map(str, nums))

        # Custom comparator
        def compare(x, y):
            return -1 if x + y > y + x else 1

        # Sort using custom logic
        nums.sort(key=cmp_to_key(compare))

        # Join into final result
        result = "".join(nums)

        # Handle case like [0, 0]
        return '0' if result[0] == '0' else result