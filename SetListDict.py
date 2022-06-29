#set deletes duplicate
#set starts with flower brackets
set_var = {"jan", "feb", "mar", "jan", "mar"}
print(set(set_var))
for element in set_var:
    print(element)
set_var.add("apr")
set_var.add("mar")
print("This is set ->", set_var)

#List wont delete duplicate
#List always starts with square brackets
my_lists = ["one", "two", "three", "two", "four"]
my_lists.remove("two")
print("This is list -> ", my_lists)

#Dictionary is key value pair
#Dictionary starts flower braces
my_dictionary = {"days":20, "unit": "hours"}
output = my_dictionary["days"]
print(output)
