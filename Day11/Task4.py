# filter the even numbers using filter function
list1 = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
new_list = list(filter(lambda x: x%2!=0, list1))
print("Odd numbers:", new_list)