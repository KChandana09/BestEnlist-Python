# Armstrong number
def getSum(num):
    if (num==0):
        return num
    else:
        return pow ((num%10), order) + getSum(num//10)

num = int(input("Enter a number :"))
order = len(str(num))
sum = getSum(num)
if (sum == int(num)):
    print(num,"is an Armstrong Number.")
else:
    print(num,"is not an Armstrong Number.")