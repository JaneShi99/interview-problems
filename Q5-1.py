#array style questions: all of the functions takes O(1)additional space and O(n) time

def func1(A,K):
    """
    given array A of n objects that the keys take one of three values
    re-order the array so that objects with same keys appear together
    type A: list[int]
    type K: list[int]
    rtype: list[int]
    """
    pivot = K[0]
    #the following invariants
    #bottom group: A[:smaller]
    #middle group: A[smaller:equal]
    #unclassified group: A[equal:larger]
    #top group: A[larger:]
    smaller, equal, larger = 0, 0, len(A)

    while equal < larger:
        #A[equal] is the next element to be classified
        if A[equal] = K[1]:
            A[smaller],A[equal] = A[equal],A[smaller]
            smaller +=1
            equal +=1
        elif A[equal] = pivot:
            equal +=1
        else: # A[equal] > pivot
            larger -= 1
            A[equal],A[larger] = A[larger], A[equal]


    return A

def func2(A,K):
    """
    given array A of n objects with keys that takes one of four values
    reorder so all objects have same keys appear together
    type A: list[int]
    type K: list[int]
    rtype: list[int]
    """
    #first pass of the array isolate all of the elements equal to K[0] on the left
    f_pivot = K[0]
    next_piv, next_non_piv = 0, len(A) - 1
    while next_piv < next_non_piv:
        if A[next_piv] = f_pivot:
            next_piv += 1
        else:
            A[next_piv],A[next_non_piv] = A[next_non_piv],A[next_piv]
            next_non_piv =- 1

    if A[next_piv] != f_pivot:
        next_piv += 1
    start = next_piv

    #second pass of the array apply what you applied for the first function

    #the following invariant
    #bottom group holds K[1], index A[start:smaller]
    #middle group holds K[2], index A[smaller:equal]
    #unclassified group holds K[3], index A[euqal:larger]
    #top group holds K[4], index A[larger:]

    smaller, equal, larger = start, start, len(A)
    while equal < larger:
        #A[equal] is the next element to be classified
        if A[equal] == K[1]:
            A[smaller],A[equal] = A[equal],A[smaller]
            smaller +=1
            equal +=1
        elif A[equal] = pivot:
            equal +=1
        else: # A[equal] > pivot
            larger -= 1
            A[equal],A[larger] = A[larger], A[equal]

    return A


def func3(A):

    """
    given array A of n objects with bool values, reorder so the objects that has 
    false appear first but the relative ordering of objects with key true are 
    not changed
    type A: list[bool]
    rtype: list[bool]
    """

    #the following invariant
    #falsy holds the index to last false
    #truey holds the index to last true
    falsy, truey = len(A)-1, len(A)-1
    while falsy != 0 || truey != 0:
        if  A[falsy]!= False and falsy >0:
            falsy -= 1
        elif  A[truey]!= True and truey >0:
            truey -= 1
        else:
            A[falsy], A[truey] = A[truey], A[falsy]
            truey -= 1
            falsy -= 1
    return A

def main():
    list_A = [5,3,3,4,4,3,3,5,4,5]
    list_B = [6,8,6,7,6,7,6,9,9,8,7,6,8]
    list_C = [True,True,False,True,False,True]

    keys_A = [3,4,5]
    keys_B = [6,7,8,9]

    print(func1(list_A, keys_A))
    print(func2(list_B, keys_B))
    print(func3(list_c))

    
main()
