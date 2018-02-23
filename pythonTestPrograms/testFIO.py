import sys

file = open("test.txt", "w")
file.write("Hello ")
file.write("World\n")
file.write("what's up?\n")
file.close()

file = open("append.txt", "a")
file.write("Hello ")
file.write("World\n")
file.write("what's up?\n")
file.close()

file = open("append.txt", "r")
print file.read()