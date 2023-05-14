#this function creates a list of odd numbers from a given sorted list
def odd_numbers(sorted_list: list) -> list:
    """
    Create a list of odd numbers from a givel list.
    :param sorted_list: sorted list
    :return: list
    """
    new_list = []

    for el in sorted_list:
        if el % 2 != 0:
            new_list.append(el)
    return new_list

#this function creates a list of elements with odd indexes
def odd_index(check_list: list) -> list:
    """
    Crete a new list from elements with odd indexes from a given list
    :param check_list: sorted list
    :return: list
    """
    new_list = []
    for i in range(len(check_list)):
        if i % 2 != 0:
            new_list.append(check_list[i])
    return new_list