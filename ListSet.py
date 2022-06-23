#set
set_var = {"jan", "feb", "mar", "jan"}
print(set(set_var))
for element in set_var:
    print(element)
set_var.add("apr")
set_var.remove("feb")
print("This is set ->", set_var)

#list
my_lists = ["one", "two", "three", "two", "four"]
my_lists.remove("two")
print("This is list -> ", my_lists)
