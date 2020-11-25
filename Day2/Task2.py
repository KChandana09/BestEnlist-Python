#create a String variable of 5 characters  and replace the 3rd character with G
string = "Tasks"
position = 2
replace_char = "G"

string = string[:position] + replace_char + string[position+1:]
print(string)
