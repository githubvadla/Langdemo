# Verify whether the number is valid mobile number or not
# Complete validation
import Lengthofstring as ls

num = input("enter the number: ")
temp = ls.find_length(num)
print(temp)
if (temp != 10) or (not num.isdigit()) or (num.startswith("0")):
    print("This is not valid mobile number")
else:
    print("this is valid mobile number")
print("Length of number", ls.find_length(num))
