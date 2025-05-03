class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        pascal = []

        for i in range(numRows):
            pascal.append([1]*(i+1))
        
        for i in range(2, numRows):
            for j in range(1, len(pascal[i])-1):
                pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]
        
        return pascal
        