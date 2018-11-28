def insert_shift_list(input_list, value_to_add):
    """This program will take argumenets, both a list, and a value to insert into the middle of that list, and will return a list with the target value inserted into the middle"""
    if type(input_list) is not list:
        raise TypeError('The first argument needs to be a list')

    list_middle = (len(input_list) // 2 + 1) - abs(len(input_list) % 2 - 1)
    return input_list[:list_middle] + [value_to_add] + input_list[list_middle:]
