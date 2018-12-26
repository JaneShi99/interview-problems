#Question 8.1

#stack that holds max 

class stack:
    #named tuple records both the element value and the corresponding max value to that 		
    #element
    
    #ElementWithCachedMax is a structure that exists within stack
    #push and pop and the operator[-1] for stack is already defined as it is
    ElementWithCachedMax = collections.namedtuple('ElementWithCachedMax',('element','max'))
    
    def __init__(self):
        #this is the array that holds the structure ElementWithCachedMax, which
        #in itself holds the value and max
        self._element_with_cached_max == []
        
    def empty(self):
        retur len(self._element_with_cached_max ) == 0
    
    def max(self):
        if self.empty():
            raise IndexError('max(): empty stack')
        return self._element_with_cached_max[-1].max
    
    def pop(self):
        if self.empty():
            raise IndexError('pop(): empty stack')
        return self._element_with_cached_max.pop().element
    
    def push(self,x):
        self._element_with_cached_max.append(
            self.ElementWithCachedMax(x, x if self.empty() else max(x,self.max()))

#stack that holds max and saves even more best case space

class Stack:
    class MaxWithCount:
        def __init__(self,max,count):
            # the MaxWithCount class is the type of objects held in _cached_max_with_count 				
	    # stack, its max field holds the value of the max element and the count is the 
            # number of occurences for the corresponding interval
            self.max, self.count = max, count
            
    def __init__(self):
        # making two stacks, one for the max and one to hold its elements
        # the stack _cached_max_with_count holds the elements of type MaxWithCount
        self._element = []
        self._cached_max_with_count = []
        
    def empty(self):
        return len(self._element) == 0
    
    def max(self):
        if self.empty():
            raise IndexError('max():empty stack')
        return self._cached_max_with_count[-1].max
    
    def pop(self):
        if self.empty():
            raise IndexError('pop():empty stack')
        pop_element = self._element.pop()
        current_max = self._cached_max_with_count[-1].max
        #if the pop element is the max, then things need to be changed
        #otherwise, if the pop element is not the max it doesnt matter when you remove it
        if pop_element == current_max:
            #one less occurence of the max
            self._cached_max_with_count[-1].count-=1
            #when it's zero then you pop it
            if self._cached_max_with_count[-1].count == 0:
                self._cached_max_with_count.pop()
        return pop_element
    
    def push(self,x):
        self._element.append(x)
        if len(self._cached_max_with_count) == 0:
            self._cached_max_with_count.append(self.MaxWithCount(x,1))
        else:
            current_max = self._cached_max_with_count[-1].max
            if x== current_max:
                self._cached_max_with_count[-1].max +=1
            elif x > current_max:
                self._cached_max_with_count.append(self.MaxWithCount(x,1))


