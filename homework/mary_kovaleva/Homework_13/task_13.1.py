import datetime
import os

base_path = os.path.dirname(__file__)
hw_path = os.path.dirname(os.path.dirname(base_path))
file_path = os.path.join(hw_path, 'eugene_okulik', 'hw_13', 'data.txt')


def read_file():
    with open(file_path) as file:
        for line in file.readlines():
            yield line


def get_time(line):
    return datetime.datetime.strptime(next(line)[3:29], '%Y-%m-%d %H:%M:%S.%f')


lines = read_file()
print(get_time(lines) + datetime.timedelta(days=7))
print(datetime.datetime.strftime(get_time(lines), "%A"))
print((datetime.datetime.now() - get_time(lines)).days)
