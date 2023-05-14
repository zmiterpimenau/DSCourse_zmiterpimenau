import random
def list_generator():
    check_list = []
    for i in range(10):
        check_list.append(random.randint(1, 100))
    return check_list