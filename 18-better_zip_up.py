#!/usr/bin/python3
""" Combining two list using zip method."""


music = ["Blues", "Country", "Electronic", "Hip hop", "Jazz", "Pop", "Rock"]
s_no = [1, 2, 3, 4, 5, 6, 7]

# Fir tuple ouput
grouping = list(zip(s_no, music))

# For dictionary output
g = dict(zip(s_no, music))

# For list output
x = [[i, j] for i, j in zip(s_no, music)]
print(grouping)
print(g)
print(x)
