def intersection_two_arrays(A,B):
    i,j,intersection = 0,0,[]
    while i < len(A) and j < len(B):
        if A[i] == B[j]:
            if i == 0 or A[i] != A[i-1]:
                #only need to check it once for A, as
                #that suffices to avoid duplicates
               	intersection.append(A[i])
            i,j = i + 1, j + 1
        elif A[i] > B[j]:
            j += 1
        else: #A[i] < B[j]
            i += 1
    return intersection

A = [1,2,3,3,3,4,5,5,5,6,7]
B = [-1,0,1,1,2,2,3,5,6,7,8,9,11,13]
print(intersection_two_arrays(A,B))
