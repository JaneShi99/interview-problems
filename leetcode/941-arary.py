class Solution:
    def validMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        
        i = 0
        n=len(A)
        
        while i < n-1 and A[i] < A[i+1]:
            i+=1
        if i==0 or i==n-1:
            return False
        while i < n-1 and A[i]>A[i+1]:
            i+=1
        return i == n-1
        
        #check if you have successfully walked i to the n-1th spot!
        #this way i serves as a counter that increments along with the walk
