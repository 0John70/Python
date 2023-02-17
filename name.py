
name1 = input("Please input name1: ")
name2 = input("Please input name2: ")
def add_names(name1,name2):
    result = name1 + name2
    print("Hello " + result)
    add_names(name1,name2)