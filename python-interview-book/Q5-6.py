def longestSub(A):
    """
    type A: list[int]
    rtype: int, the length of the longest subarray of A
    """
    longestSubSoFar, subArrAccum = 1,1
    for i in range(1,len(A),1):
        if A[i] == A[i-1]:
            subArrAccum += 1
        else:
            if subArrAccum > longestSubSoFar:
                longestSubSoFar = subArrAccum
            subArrAccum = 0
    return longestSubSoFar


def main():
    print(longestSub([1,2,2,2,2,3,3,3,3,3,3,3,4,4,4,2,3,2,3,2,1,4,5,5]))

main()
