# Fibonacci sequence
n = int(input("Enter the value of n: "))
a, b = 0, 1
sum = 0
count = 1
print("Fibonacci Sequence is: ", end = " ")
while(count <= n):
  print(sum, end = " ")
  count += 1
  a = b
  b = sum
  sum = a + b