import random
from apps import (
    list_generator,
    my_list_sorting,
    odd_numbers,
    odd_index
)
from text_constructors import (
    write_text,
    add_text
)
from data import (
    task_one,
    task_two,
    task_three
)

check_list = list_generator()
final_list = my_list_sorting(check_list)
odd_values_list = odd_numbers(final_list)
odd_index_list = odd_index(final_list)

write_text(check_list, final_list, task_one)
add_text(final_list, odd_values_list, task_two)
add_text(final_list, odd_index_list, task_three)
#%%
