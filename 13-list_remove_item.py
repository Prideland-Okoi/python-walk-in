#!/usr/bin/python3
""" Removing all occurences of an item from a list"""
my_list = ["Perl", "Ruby", "C#", "Go", "Swift", "Ruby", "C++", "Kotlin"]
item = "Ruby"
my_list = [x for x in my_list if x != item]
print(my_list)
