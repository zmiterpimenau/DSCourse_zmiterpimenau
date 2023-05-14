#simple function to create a function which sorts a list from lower to higher element.
#it creates a new sorted list without changing original one
def my_list_sorting(check_list: list) -> list:
    """
    Simple sorting function from min to max value in the list
    :param check_list: unsorted list
    :return: sorted list
    """
    final_list = []
    final_list = [final_list.append(0) for i in range(len(check_list))]
    counter = 0

    for i in range(len(check_list)):
        #additional check to find if there are equal elements in the checking list
        if check_list[i] in final_list:
            add_index = final_list.count(check_list[i])
            counter += add_index

        #this loop counts how many elements are lower than the one under check.
        for j in range(len(check_list)):
            if check_list[i] > check_list[j]:
                counter += 1

        #number of lower element is the index of checking element in final list
        final_list[counter] = check_list[i]
        counter = 0
    return final_list

#after googling

#bubble sorting - checking pairs of elements
#returns sorted list without creating a new one
def bubble_sort(check_list: list) -> list:
    """
    Returns sorted list without creating a new one = checked_list will change elements
    :param check_list: list
    :return: the same list but sorted
    """
    #flag is in position True to start the loop
    flag = True
    while flag:
        flag = False
        for i in range(len(check_list) - 1):
            if check_list[i] > check_list[i+1]:
                #change 2 elements with each other
                check_list[i], check_list[i+1] = check_list[i+1], check_list[i]
                #return flag to True for the next itertion
                flag = True
    return check_list

#selection sort - divides a list into two segments (sorted and unsorted)
# checks each element from a sorted segment with elements in unsorted segment
# changes elements if lower
def selection_sort(list_for_sort: list) -> list:
    """
    Sorting of the list with selection method
    :param check_list: list
    :return: the same list but sorted
    """
    #i is number of sorted values
    for i in range(len(list_for_sort)):
        # first element is the lowest b default
        lowest_value_index = i
        # iterate unsorted elements
        for j in range(i+1, len(list_for_sort)):
            if list_for_sort[j] < list_for_sort[lowest_value_index]:
                lowest_value_index = j
        # the lowest element changes its position with the first from the list
        list_for_sort[i], list_for_sort[lowest_value_index] = list_for_sort[lowest_value_index], list_for_sort[i]
    return list_for_sort