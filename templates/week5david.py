# Challenge 1: Name the variable types of the following variables. Print them out into console in the format "Variable: Variable Type" (might have to google "how to print variables in python")
var1 = 3
var2 = "Mr. Mortensen"
var3 = 'f'
var4 = 0.4
print(var1, ": ", "Integer")
print(var2, ": ", "String")
print(var3, ": ", "Character")
print(var4, ": ", "Float")
print('')


# Challenge 2: Pass list1 into list2. However, list2 must contain the elements of list1 in order. Print list2. +0.3 if you can create a function to order a list and can display it on your website
from random import randint
list1 = [5, 3, 4, 1, 2]
print("list1: ", list1)
def orderList1(list):
    nlist = []
    for i in range(len(list)):
        nlist.append(min(list))
        list.remove(min(list))
    return nlist
list2 = orderList1(list1)
print('list2: ', list2)
print('')

# Challenge 3: Find a way to add 3 to each element in the array. Then, take the average of the array and put it into the variable avg. +0.2 if you can turn this into a function and display it on your website.
averageList = [23, 41, 90, 55, 71, 83]
def addInt(list, n):
    nlist = []
    for i in range(len(list)):
        nlist.append(list[i] + n)
    return nlist

def average(list):
    return sum(list)/len(list)

list3=addInt(averageList, 3)
print(averageList)
print(list3)
avg = average(list3)
print(avg)

