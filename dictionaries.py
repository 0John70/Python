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

# print(profile)
profile = {}
def register (): 
    username = input("Please input username: ")
    email = input("Please input email: ")
    password = input("Please input password: ")

    profile["username"] = username
    profile["email"] = email  
    profile["password"] = password

def get_profile():
    print(profile)

def change_username():
    new_username = input("Enter new username: ")
    profile["username"] = new_username
register()
get_profile()

change_username()
get_profile()