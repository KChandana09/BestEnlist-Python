#merge two Python dictionaries
sweets = {"Jamun": 25, "Jalebi": 20, "Rasagulla": 40}
chocolates = {"Dairy Milk": 30, "Kit Kat": 25, "Eclairs": 45}
pack = sweets.copy()
pack.update(chocolates)
print(pack)