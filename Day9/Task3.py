#multiply each number of given list with a given number
nums = [4, 6, 8, 10, 12]
n = 5
filtered_numbers=list(map(lambda number:number*n,nums))
print(' '.join(map(str,filtered_numbers)))