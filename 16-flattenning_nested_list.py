#!/usr/bin/python3
""" Flattenning a nested list."""

my_list = ["air", "water", "oil"], [2, 4, 5], ["Ra", 6, "Zeus"]
f_list = [x for sub_list in my_list for x in sub_list]
print(f_list)
