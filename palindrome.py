age1 = 21
age2 = 16
print(age1, age2)
# Python program to swap two variables


# To take inputs from the user
#x = input('Enter value of x: ')
#y = input('Enter value of y: ')

# create a temporary variable and swap the values
temp = age1
age1 = age2
age2 = temp

print('The value of x after swapping: {}'.format(age1))
print('The value of y after swapping: {}'.format(age2))