list1 = [
    "Great Work!",
    "Well Done!",
    "Great, now aim for that 100!"

]

list2 = [
    "Not bad, now aim for that 90!",
    "Good Job!"
]

list3 = [
    "A C isn't too bad nor is it too good. Go for that 80!",
    "Mediocre Job, got to try harder next time."
]

list4 = [
    "Barely a passing grade. Go for that 80!",
    "Did you actually try? Didn't think so."
]

list5 = [
    "An F, really?",
    "Someone didn't study."
]

input1 = int(input("What did you get on your test?"))
score = input1

if score >= 90:
    import random
    print(random.choice(list1))
elif score >= 80:
    import random
    print(random.choice(list2))
elif score >= 70:
    import random
    print(random.choice(list3))
elif score >= 60:
    import random
    print(random.choice(list4))
else:
    if score >= 0:
        import random
        print(random.choice(list5))
