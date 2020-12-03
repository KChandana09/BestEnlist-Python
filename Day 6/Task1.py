list = [10,20,30,40,50]

print("List before: " + str(list))

for i in range(len(list)):
      list[i] = list[i] + 2    # add +2 to every element in list

print("List after: "+ str(list))