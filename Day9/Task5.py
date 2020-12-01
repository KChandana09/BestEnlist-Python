#count the even numbers in a given list of integers 
list1 = [2, 4, 9, 15, 16, 20]  

even_count = len(list(filter(lambda x: (x % 2 == 0), list1)))
  
print("Count of even numbers in the list: ", even_count)  