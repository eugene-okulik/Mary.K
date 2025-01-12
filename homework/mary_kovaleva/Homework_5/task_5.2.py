str1 = 'результат операции: 42'
str2 = 'результат операции: 514'
str3 = 'результат работы программы: 9'

num1_index = str1.index(':')
num2_index = str2.index(':')
num3_index = str3.index(':')

num1 = int(str1[num1_index + 2:])
num2 = int(str2[num2_index + 2:])
num3 = int(str3[num3_index + 2:])

print(num1 + 10, num2 + 10, num3 + 10, sep='\n')
