# by connor arch david

def swapAge(ageOne, ageTwo):
    if ageOne < ageTwo:
        tuple = (ageOne, ageTwo)
    else:
        tuple = (ageTwo, ageOne)
    return tuple

age1 = input("What is your age?")
age2 = input("What is their age?")

print(age1, age2)
print(swapAge(age1, age2))
