#My first python list
numbers = [10,30,20,10,5,1]
names = ["python","java"]

#To get the length of my list
print(len(numbers))

#to get the sum
print(sum(numbers))
print(len(numbers))#get the length of my list

for i in range(len(numbers)):
    print(numbers[i])

#TYPES OF LISTS

#INDEX-

print (names . index ("java"))
print(numbers.index(30))

#APPEND-adds an element to the end of a list

# Before appending
for i in range (len(numbers)):
    print(numbers[i])
    numbers.append(5)

    print("\n")

#After appending
    for i in range(len(numbers)):
        print(numbers[i])
#SORT- arranges the elements in ascending order

for i in range (len(numbers)):
    print(numbers[i])
    # sort the list

    numbers.sort()
#Add a new line for formatted output
print("\n")

#COUNT-returns the number of times an element occurs on a list

print(numbers . count (30))

#POP -removes an element at a given index and returns that element

print (numbers . pop(5))

#INSERT-inserts an element x at an index y

numbers . insert(3,50)
for i in range (len (numbers)):
    print(numbers[i])
# REMOVE-removes the  first occurence

print(numbers.remove(10))

# TIPS AND TRICKS
 
#  Multiplying a list

zeros = [0]* 10
print(zeros)

# #adding lists

list1 = [169,60]
list2 = [39,58]
print (list1 + list2)

# #Slicing a list
nums = [23,43,78,88]
nums [2:]
[78,88]

#  #get the maximum value


max(nums)
# #get the minimum value
min(nums)

# # Creating lists
nums = [] #empty list
for i in range (10):

    nums . append(i)
# for i in range (len(nums)):
    print (nums[i])
 
