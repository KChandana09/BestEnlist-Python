#numbers divisible by 9 from a list of numbers
list1 = [9, 15, 35, 45, 56, 72, 91, 100]

result = list(filter(lambda x: (x % 9 == 0), list1))

print("Numbers divisible by 9 are",result)