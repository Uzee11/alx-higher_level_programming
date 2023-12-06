#!/usr/bin/python3

def search_replace(my_list, search, replace):
    # Create a new list with the replaced elements
    new_list = [replace if element == search else element for element in my_list]
    return new_list

# Example usage:
original_list = [1, 2, 3, 2, 4, 2, 5]
element_to_replace = 2
replacement_element = 99

new_list = search_replace(original_list, element_to_replace, replacement_element)
print(new_list)
