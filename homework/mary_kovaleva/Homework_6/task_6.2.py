for i in range(1, 101):
    a = 'Fuzz' * (i % 3 == 0) + 'Buzz' * (i % 5 == 0)
    if a:
        print(a)
    else:
        print(i)
