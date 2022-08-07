list_ = [
    {'name': 'Alex', 'age': 25},
    {'name': 'Oleg', 'age': 23},
    {'name': 'Anna', 'age': 32},
    {'name': 'Igor', 'age': 50},
    {'name': 'Anton', 'age': 17},
]

def list_filter(list_):
    new_list = []
    for d in list_:
        if d['name'].startswith('A') and d['age'] >= 18 and d['age'] <= 30:
            new_list.append(d)
        else:
            continue
    return new_list


if __name__ == '__main__':
    print(list_filter(list_))
