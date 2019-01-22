import functools
#getting familiar with the library function: functools.reduce function in python
#prototype: reduct(function, iterable [,initial value])
#it applies the function, starting at initial value, and then iterate through the iterable
#the function might be binary
def reduce(function, iterable, initializer=None):
    it = iter(iterable)
    if initializer is None:
        value = next(it)
    else:
        value = initializer
    for element in it:
        value = function(value, element)
    return value

#note that: the order of the operation goes like: for binary function it takes initialized value as
#the first of the lambdas, and then pass thru iterables
#note that the lambda function should be a binary function
ans = functools.reduce(lambda x, y: x+y, [0,1,2,3,4],20)
ans2 = functools.reduce(lambda x, y: x * y, [1,2,3,4,5,6,7],20)
print(ans)
print(ans2)
print(ans3)
