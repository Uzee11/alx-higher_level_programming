#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    # Use symmetric_difference to get elements present in only one set
    result_set = set_1.symmetric_difference(set_2)
    return result_set

# Example usage:
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

result = only_diff_elements(set_a, set_b)
print(result)
