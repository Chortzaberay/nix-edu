list_ = [{'name': 'Oleg', 'age': 23}, {'name': 'Vasya', 'age': 19}]

new_list = sorted(list_, key=lambda x: x['age'])
print(new_list)

