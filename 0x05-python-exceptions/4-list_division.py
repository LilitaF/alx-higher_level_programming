#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    list_result = []
    for i in range(list_length):
        element1 = 0
        element2 = 0
        try:
            if i < len(my_list_1):
                element1 = my_list_1[i]
            if i < len(my_list_2):
                element2 = my_list_2[i]

            if not isinstance(element1, (int, float)) or not isinstance(element2, (int, float)):
                raise TypeError("wrong type")
            if element2 == 0:
                raise ZeroDivisionError("division by 0")
            
            result = element1 / element2
            list_result.append(result)

        except TypeError:
            print("wrong type")
            list_result.append(0)
        except ZeroDivisionError:
            print("division by 0")
            list_result.append(0)
        except IndexError:
            print("out of range")
            list_result.append(0)
        finally:
            pass

    return (list_result)
