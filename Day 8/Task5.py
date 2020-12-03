def temp(var):
   try:
      print(int(var))
   except ValueError:
      print ("The argument does not contain numbers\n")

temp(123)
temp(xyz)