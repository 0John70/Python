# name ="climate"
##index
# # x = name[-1]
# print (x)
# #To get the length of a string
# print(len(name))

# for letter in name:
#     print(letter)

# print("-" *5)

# String methods
# Upper and lower
# name = "JOHN"
# print(name.lower())

# #Checking for alphanumeric
# password = input("Please input password: ")
# if password.isalpha():
#     print("Invalid password")
# else:
    # print("Valid password")

#Ask for user name
# Print "hello user name"
# name = input("Please input user name:")

# print ("Hello " + name.upper())
# Slicing a string


# name = "kingajohn"
# print(name[5:9])

string = input("please input string:")
print("The length of the string is:",len(string))

print(string *10)

print("The first characters of the string is:",string[0])

first_three = string[:3]
print("The first three charactes are:",first_three)

last_three =string[-3:]
print("The last three characters are:",last_three)


print("The string in reverse:",string[::-1])

print("The seventh character is:",string[6])

print("The string without the last character:",string[:-1:])
print("The string without the first character:",string[1::])

print(string.upper())
