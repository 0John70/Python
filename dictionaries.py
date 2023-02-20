# company = {"name": "Amazon",
            # "year": 1994
# }   

# print(company.get("name"))
# company.update({"name":"shopify"})
# print(company.get("name"))

# company . update({"year":"2006"})
# print(company.get("year"))


# cars = {"prado":{"model": "2015 "},
        # "x_trail":{"model":"2017 "}
# }
# print(cars("x_trail","model"))

# first_name = input("please input name:")
# def hello (first_name):
    # print("Hello " + first_name)
# # hello(first_name)
  
# cars = {
# #         "model":"ford",
#         "year" : 1988,
#         "color": "red",
#         "country":"Kenya"
# }

# print(cars["year"])

# person = {
#     "name":"Blair",
#     "age":31,
#     "pets":{
#         "dog":"x",
#         "cat":"y"

#     }
# }
# print (person["pets"]["cat"])


# profile = {}
# profile["username"] = "user123"
# # profile["age"] = 21
# profile["email"] = "user123@gmail.com"

# # print(profile)

# profile = {}
# def register (): 
#     username = input("Please input username: ")
#     email = input("Please input email: ")
#     password = input("Please input password: ")

#     profile["username"] = username
#     profile["email"] = email  
#     profile["password"] = password

# def get_profile():
#     print(profile)

# def change_username():
#     new_username = input("Enter new username: ")
#     profile["username"] = new_username
# register()
# get_profile()

# change_username()
# get_profile()

# Dictionary methods
# 1 clear
# 2 pop 
# 3 keys
# 4 values
# 5 get
# 6 popitem
# 7 update

##no 1 and no 2
# # initialize an empty dictionary to store product names and prices
# initialize an empty dictionary to store product names and prices
# products = {}

# # loop to allow the user to enter product names and prices
# while True:
#     name = input("Enter product name (or 'q' to quit): ")
#     if name == 'q':
#         break
#     price = input("Enter price: ")
#     products[name] = float(price)

# # prompt the user to enter a dollar amount

#  max_price = float(input("Enter the maximum price: "))

# # loop through the products and print out those whose price is less than the maximum price
# print("Products that cost less than $%.2f:" % max_price)
# for name, price in products.items():
#     if price < max_price:
#         print(f"{name}: ${price:.2f}")


##no 3
# define the dictionary of month names and days
month_days = {
    'January': 31,
    'February': 28,
    'March': 31,
    'April': 30,
    'May': 31,
    'June': 30,
    'July': 31,
    'August': 31,
    'September': 30,
    'October': 31,
    'November': 30,
    'December': 31
}

# (a) prompt the user to enter a month name and print out the number of days in the month
month = input("Enter a month name: ")
days = month_days.get(month, None)
if days is None:
    print("Invalid month name.")
else:
    print(f"{month} has {days} days.")

# (b) print out all of the keys in alphabetical order
print("Month names in alphabetical order:")
for name in sorted(month_days.keys()):
    print(name)
# (c) print out all of the months with 31 days
print("Months with 31 days:")
for name, days in month_days.items():
    if days == 31:
        print(name)

# (d) print out the (key-value) pairs sorted by the number of days in each month
print("Month names and days sorted by number of days:")
for name, days in sorted(month_days.items(), key=lambda x: x[1]):
    print(f"{name}: {days}")
