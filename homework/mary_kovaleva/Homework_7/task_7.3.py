result1 = 'результат операции: 42'
result2 = 'результат операции: 54'
result3 = 'результат работы программы: 209'
result4 = 'результат: 2'


def get_num(string):
    num = int(string.split(': ')[-1])
    print(num + 10)


get_num(result1)
get_num(result2)
get_num(result3)
get_num(result4)
