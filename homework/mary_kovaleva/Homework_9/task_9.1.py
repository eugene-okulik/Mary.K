import datetime

date = "Jan 15, 2023 - 12:05:33"
py_date = datetime.datetime.strptime(date, "%b %d, %Y - %H:%M:%S")
month = datetime.datetime.strftime(py_date, "%B")
new_date = datetime.datetime.strftime(py_date, "%d.%m.%Y, %H:%M")
print(month, new_date, sep="\n")
