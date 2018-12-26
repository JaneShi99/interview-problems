def is_balanced_binary_tree(tree):
    BalancedStatusWithHeight = collections.namedtuple('BalancedStatusWithHeight', ('balanced','height'))    
    #first value tells you whether it is balanced
    #second value tells you its heighti

    #this is the return type that gives you a structure to work with, where it contains useful information for
    #both return and for the numeric check

    #you expect BalancedStatusWithHeight return type for all of the returns in the helper recursive fuction and eventually
    #you return the field of the tree in that function
    def check_balanced(tree):
        if not (tree):
            return BalancedStatusWithHeight(True, -1) #base case for a null node
        left_result = check_balanced(tree.left)
        if not left_result.balanced:
            return BalancedStatusWithHeight(False,0)

        right_result = check_balanced(tree.right)
        if not right_result.balanced:
            return BalancedStatusWithHeight(False,0)

        is_balanced = abs(left_result.height - right_result.height) <= 1
        height = max(left_result.height,right_result.height) + 1
        return BalancedStatusWithHeight(is_balanced,height)
    return check_balanced(tree).balanced

	
def largest_complete_subtree(tree):
    CompleteStatusWithHeight = collections.namedtyple('CompleteStatusWithHeight',('complete','height'))
    #first value tells you whether the tree is complete
    #second value tells you the height of largest complete subtree so far
    def check_complete(tree):
        if not tree:
            return  CompleteStatusWithHeight(True,-1) #base case
        left_result = check_complete(tree.left)
        right_result = check_complete(tree.right)
        if not (left_result.complete or right_result.complete):
            return CompleteStatusWithHeight(False, max(left_result.height,right_result.height))
        if not (left_result.height == right_result.height):
            return CompleteStatusWithHeight(False, max(left_result.height,right_result.hright))
        else:
            return CompleteStatusWithHeight(True, left_result.height + 1)
    return check_complete(tree).height

def check_k_balanced(tree, k):
    BalancedStatusWithHeight = collecions.namedtuple('BalancedStatusWithHeight',('balanced','height'))
    def check(tree):
        if not tree:
            return BalancedStatusWithHeight(True, -1) # base case if it is a null tree
        left_result = check(tree.left)
        if not left_result.balanced:
            return BalancedStatusWithHeight(False, 0)
        right_result = check(tree.right)
        if not right_result.balanced:
            return BalancedStatusWithHeight(False, 0)
        is_balanced = abs(left_result.height - right_result.height) <= k
        height = max(left_result.height, right_result.height) + 1
        return BalancedStatusWithHeight(is_balanced,height)
    return check(tree)

