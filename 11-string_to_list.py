#!/usr/bin/python3
""" Converting list to string"""

string = "Dummy head"
my_str = "".join(string.split())  # To remove whitespace
my_list = list(my_str)
print(my_list)
