import random

salary = int(input("Enter your salary: "))
bonus = random.choice((True, False))
if bonus:
    salary += int(random.random() * 1000)
print(salary)
