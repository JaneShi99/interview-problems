#design an algorithm that takes a sorted array and a key, find the index of first occurence of an element greater than that key

def search_greater(A,k):
    """
    type A: int array
    type k: int
    rtype: int
    """
    left,right,res = 0,len(A)-1,len(A)-1
    while left <= right:
        mid = (left + right) // 2
        if A[mid] > k:
            right = mid - 1
        elif A[mid] == k:
            res = mid
            left = mid + 1
        else: #A[mid] < k
            left mid + 1
    return result + 1

# Let A be unsorted array of length n. A[0] >= A[1] and A[n-2] <= A[n-1]
# call an index i a local minimum if A[i] is less than or equal to its neighbours
# how would you efficiently locate the local minimum if it exists?


def get_a_local_mim(A):
    """
    type A: int array
    rtype: int
    """
    # idea: use binary search. use the fact that A[0]>=A[1] and A[n-1]<=A[n-1]
    # note that either the middle is the local min, or the three adjacent items are in 
    # ascending (then there is a local min to its left) or descending (then there is a local min to its right) order
    left,right,res = 0,len(A) - 1, -1
    while left <= right:
        mid = (left + right) // 2
        if A[mid-1]<=A[mid] and A[mid]<=A[mid+1]:
            return mid
        elif A[mid-1]<=A[mid]:
            right = mid-1
        else: # A[mid]>=A[mid
            left = mid + 1
    return res

#return an integer that returns the interval enclosing k, given A(array) and  k(key)
def get_interval(A,k):
    if bsearch(A,k) == -1:
        return -1
    else
        return [bsearch(A,k),search_greater(A,k)-1]


#tests if p is a prefix of a string in a array of sorted strings
def search_string(A,target):
    i = bisect.bisect_left(s(0) for s in A ,p)
    return 0<=i<=len(A) and A[i](0) == p


