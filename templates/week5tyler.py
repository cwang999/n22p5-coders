# Challenge 1: Name the variable types of the following variables. Print them out into console in the format "Variable: Variable Type" (might have to google "how to print variables in python")
var1 = 3
var2 = "Mr. Mortensen"
var3 = 'f'
var4 = 0.4
print(var1, ": Integer")
print(var2, ": String")
print(var3, ": Character")
print(var4, ": Double")

# Challenge 2: Pass list1 into list2. However, list2 must contain the elements of list1 in order. Print list2. +0.3 if you can create a function to order a list and can display it on your website

list1 = [5, 3, 4, 1, 2]
list2 = list1
def orderList(list):
    if len(list) <= 1:
        return list
    for i in range(len(list)):
        list[i] = i + 1
    return list

list2 = orderList(list1)
print(list2)

# Challenge 3: Find a way to add 3 to each element in the array. Then, take the average of the array and put it into the variable avg. +0.2 if you can turn this into a function and display it on your website.

avgList = [23, 41, 90, 55, 71, 83]
def averageList(list):
    if len(list) <= 1:
        return list
    for i in range(len(list)):
        list[i] += 3
    return list
avgList = averageList(avgList)
avg = (avgList[0] + avgList[1] + avgList[2] + avgList[3] + avgList[4] + avgList[5]) / 6
print(avg)