my_dict = {'tuple': (1, 2, 3.14, 'text', False), 'list': [1, 2.5, 'text', [1, 2, 3], True], 'dict': {1: 'one', 2: 'two',
           3: 'three', 4: 'four', 'five': (78, 54, 12, 0, 78)}, 'set': {1, 0.5, 123, (1, ), 'text'}}

print(my_dict['tuple'][-1])

my_dict['list'].append('last')
my_dict['list'].pop(1)

my_dict['dict']['i am a tuple'] = (1, 2, 3, 4, 5)
my_dict['dict'].pop(1)

my_dict['set'].add(432)
my_dict['set'].remove(1)

for k, v in my_dict.items():
    print(f"В ключе {k} хрянятся такие данные как {v}")
