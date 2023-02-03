import random
from collections.abc import Set as _Set, Sequence as _Sequence

def create_random_id(id_size: int, min_value: int, max_value: int):
    range_size = max_value - min_value + 1
    
    if(range_size < id_size):
        return None
    
    value_set = {str(i) for i in range(min_value, max_value+1)}

    if(range_size ==  id_size):
        return value_set
    
    if(id_size <= range_size / 2):
        secondary_result_list = random.sample(value_set, id_size)
        secondary_result_set = set()
        secondary_result_set.update(secondary_result_list)
        value_set = secondary_result_set
    else:
        print(range_size - id_size)
        elements_to_remove = random.sample(value_set, range_size - id_size)
        for item in elements_to_remove:
            value_set.remove(item)
    return value_set

answer = create_random_id(80, 10, 1000)
print(answer)
print(len(answer))
