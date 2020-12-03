# merge two lists into list of tuples
list1 = ['sweets', 'chocolates', 'icecreams'] 
list2 = [20, 30, 40] 

merged_list = list(zip(list1, list2))  

print(merged_list)