import random

def task2():
    my_dict = {0: 10, 1: 20}
    thing = input("Enter a new value: ")
    my_dict[2] = thing
    print(my_dict)

def task3():
    dic1={1:10, 2:20}
    dic2={3:30, 4:40}
    dic3={5:50,6:60}
    dic4={}
    for d in (dic1, dic2, dic3):
        dic4.update(d)
    print(dic4)

def task4():
    dic4 = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
    key = int(input("Enter a key: "))
    if key in dic4:
        print("Key exists")
    else:
        print("Key does not exist")

def task5():
    d = {'x': 10, 'y': 20, 'z': 30}
    for dict_key, dict_value in d.items():
        print(dict_key, "->", dict_value)

def task6():
    thing = int(input("Enter a number: "))
    my_dict = {}
    for x in range(1, thing + 1):
        my_dict[x] = x * x
    print(my_dict)


task6()