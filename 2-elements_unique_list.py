#!/usr/bin/python3
"""
Checking if all item in a list are unique
"""
my_list = ["Mocha", "Pistachio", "Cookie Dough", "Ube", "Teaberry", "Ube"]

if len(my_list) == len(set(my_list)):
    print("All item are unique")
else:
    print("You have repeated items")
