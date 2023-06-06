#!/usr/bin/python3
for i in range(0, 101):
    if i < 99:
        print("{:02}".format(i), end=", ")
    if i == 99:
        print("{:02}".format(i), end="\n")
