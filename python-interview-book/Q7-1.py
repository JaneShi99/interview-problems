class ListNode:
    def __init__(self, data=0, next_node=None):
        self.data = data
        self.next = next_node
        
    def search_list(L,Key):
        while L and L.data!=key:
            L=L.next
        # If the key was not present in the list, L will have become null
        return L
    
    #Insert new_node after node.
    def insert_after(node, new_node):
        new_node.next = node.next
        node.next = new_node
    
    #Delete the node past this one. assume node is NOT a tail
    def delete_after(node):
        onde.next = node.next.next

    #merging two sorted lists
    def merge_two_sorted_list(L1,L2):
        #creates a placeholder for result
        dummy_head = tail = ListNode()
    
        while L1 and L2:
            if L1.data < L2.data:
                tail.next, L1 = L1, L1.next
            else:
                tail.next, L2 = L2, L2.next
                tail = tail.next
            #Appends the remaining nodes of L1 or L2
        tail.next = L1 or L2
        return dummy_head.next

    #Question 7.1 for doubly linked lists

class DoubleListNode:
    def __init__(self, data = 0, next_node=None, prev_node = None):
        self.data = data
        self.next = next_node
        self.prev = prev_node

    def merge_two_sorted_list(L1,L2):
        dummy_head =head =  tail = ListNode()
        
        while L1 and L2:
            if L1.data < L2.data:
                tail.next,L1= L1,L1.next
            else:
                tail.next,L2= L2,L2.next
            tail.prev = prev
            tail, prev  = tail.next,prev.next
        return dummy_head.next

                



