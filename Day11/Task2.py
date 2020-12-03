# merge the given list and the range together to create a new list of tuples.
list1=[1,2,3,4,5,6,7,8,9]

rng1 = list(range(1,8))
lst = list(zip(list1, rng1))

print(lst)