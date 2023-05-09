#!/usr/bin/python3
""" Getting the value from dictionary."""


milkshakes = {1: "Banana", 2: "Date", 3: "Chocolate", 4: "Peach", 5: "Mango"}
more_shakes = {6: "Vanilla", 7: "Coffee", 8: "Peanut Butter", 9: "Strawberry"}

sorted_value = milkshakes.values()
print(sorted_value)

sorted_val = [x for x in milkshakes.values()]
print(sorted_val)

for key, value in milkshakes.items():
    print(value)
