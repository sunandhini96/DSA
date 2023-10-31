class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows==0:
            return []
        list1=[]
        for n in range(numRows):
            row=[1]*(n+1)
            for j in range(1,n):
               row[j]=list1[n-1][j-1]+list1[n-1][j]
            list1.append(row)
        return list1
