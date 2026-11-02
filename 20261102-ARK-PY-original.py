#20261102-ARK-PY

#Task 1

name = str(input("please enter your name: "))

vaild = False
score = 0

while vaild == False:
    value = int(input("please enter your value: "))
    if 2 <= value and value <= 12:
        vaild = True

print("welcome! ", name)
print(f"{name}, you need to finish a multiplication table task!")

tasknum = int(input("how many tasks do you want to answer?"))

print(f"you will be needed to enter your answer for each task, once you finished one task, you could move to the next one, there are {tasknum} tasks in total")

mixedset = input("Mixed questions? True or False: ").strip().lower() == "true"

import random

if mixedset == False:
    for b in random.sample(range(10), tasknum):
        actanswer = value * b
        for attempts in range(3):
            uranswer = int(input(f"{value} X {b} = "))

            if uranswer == actanswer:
                score += 1
                print("Correct!")
                break
            elif uranswer < actanswer:
                print(f"{name}, your answer is too small")
            else:
                print(f"{name}, your answer is too large")
        else:
            print(f"The correct answer is {actanswer}")

    print(f"{name} your score is {score}/{tasknum}")
    if score == tasknum:
        print("Well done full marks")
    else:
        print("Have another practice")
else:
    for b in random.sample(range(10), tasknum):
        a = random.randint(1, 12)
        actanswer = a * b

        for attempts in range(3):
            uranswer = int(input(f"{a} X {b} = "))

            if uranswer == actanswer:
                score += 1
                print("Correct!")
                break
            elif uranswer < actanswer:
                print(f"{name}, your answer is too small")
            else:
                print(f"{name}, your answer is too large")
        else:
            print(f"The correct answer is {actanswer}")

    print(f"{name}, your score is {score}/{tasknum}")
    if score == tasknum:
        print("Well done full marks")
    else:
        print("Have another practice")