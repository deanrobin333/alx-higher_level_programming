#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result = []
    for idx in range(list_length):
        try:
            div = my_list_1[idx] / my_list_2[idx]
        except ZeroDivisionError:
            div = 0
            print("division by 0")
            continue
        except TypeError:
            div = 0
            print("wrong type")
            continue
        except IndexError:
            print("out of range")
            div = 0
        finally:
            result.append(div)
    return result
