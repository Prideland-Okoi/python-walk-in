#!/usr/bin/python3
""" Creating  a nested list."""

my_list = ["air", "water", "fire", "sand"]
my_list1 = [2, 4, 5]
my_list2 = ["Dozen", 12, 'XXIV']
updated_list = [[x for x in my_list], [y for y in my_list1], [z for z in my_list2]]
print(updated_list)
