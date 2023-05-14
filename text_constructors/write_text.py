def write_text(original_list, result, task):
    """
    This function re-writes existing file (if any)
    :param original_list: list before changes
    :param result: list after changes
    :param task: text of the homework task
    :return: adding some text to the file results.txt
    """
    with open("/home/dzmitry/Рабочий стол/homewars/DSCourse_zmiterpimenau/data/results.txt", "w") as file:
        file.write(f"\n{task}\n"
                   f"_______________________________________________________\n"
                   f"Original list:{original_list}.\nResult: {result}.\n")
