import sys
sys.set_int_max_str_digits(100000)


def fibonacci():
    num1 = 0
    num2 = 1
    while True:
        yield num1
        num1, num2 = num2, num1 + num2


count = 1
for num in fibonacci():
    if count in (5, 200, 1000, 100000):
        print(num)
        if count == 100000:
            break
    count += 1
