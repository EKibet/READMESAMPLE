#!/usr/bin/env python

# Module that randomizes items in a list.
from random import shuffle

# Opens a text file with names of students
with open('random.txt') as names:
  class_names = names.readlines()

# print(class_names)

# Strips the line breaks
name_list = [name.strip() for name in class_names]
# print(name_list)

first_half = name_list[:len(name_list)//2]
# print(first_half)
second_half = name_list[len(name_list)//2:]

# Randomizes the name list
shuffle(first_half)
shuffle(second_half)

# Transforms the two list into a list with tuples with pairs
pair_list = list(zip(first_half, second_half))
print(pair_list)

# Creates and writes the name of pairs
with open("random_pair.txt", "w") as output_file:
  # Iterates through the list and then extracts the names from the tuples. Puts the pair in new lines.
  output_file.write('\n'.join('{}, {}'.format(x[0], x[1]) for x in pair_list))

# print(output_file)