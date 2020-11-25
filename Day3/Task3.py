#mapping two lists into a dictionary
sweets = ['Jamun', 'Jalebi', 'Rasagulla']
quantity = [25, 20, 40]
pack = dict(zip(sweets, quantity))
print(pack)

