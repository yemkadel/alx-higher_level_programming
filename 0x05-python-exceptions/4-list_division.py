#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for num in range(0, list_length):
        try:
            res = my_list_1[num] / my_list_2[num]
            new_list.append(res)
        except ZeroDivisionError:
            print("division by 0")
            new_list.append(0)
            continue
        except TypeError:
            print("wrong type")
            new_list.append(0)
            continue
        except IndexError:
            print("out of range")
            new_list.append(0)
            continue
    return new_list
