def add_text(original_list, result, task):
    """
    This function adds some text to the existing file
    :param original_list: list before changes
    :param result: list after changes
    :param task: text of the homework task
    :return: adding some text to the file results.txt
    """
    with open("/home/dzmitry/Рабочий стол/homewars/DSCourse_zmiterpimenau/data/results.txt", "a") as file:
        file.write(f"\n{task}\n"
                   f"_______________________________________________________\n"
                   f"Original list:{original_list}.\nResult: {result}.\n")