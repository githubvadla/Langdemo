# Check the blanks in Strings
# Length of a string without using builtin function
def find_length(str):
    counter = 0
    my_list = list(str)
    for itr in my_list:
        counter = counter + 1
    return counter
