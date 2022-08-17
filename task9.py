

def my_generator(start, end):
    tmp = start
    while tmp <= end:
        yield tmp
        tmp += 1


for i in my_generator(1, 3):
    print(i)
