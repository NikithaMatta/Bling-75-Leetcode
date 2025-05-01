class Solution(object):
    def plusOne(self, digits):
        num = 0
        for digit in digits:
            num = num * 10 + digit                
        num += 1
        return [int(digit) for digit in str(num)]