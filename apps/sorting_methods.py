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