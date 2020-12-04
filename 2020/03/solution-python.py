#!/usr/bin/env python3


def part_2(coordinates):
  max_len = len(coordinates[0])
  
  paths = [
    [1, 1],
    [3, 1],
    [5, 1],
    [7, 1],
    [1, 2]
  ]

  last_index = len(coordinates)
  total = 1

  for path in paths:
    counter = 0
    idx = 0
    x_axis_pos = 0

    while idx < last_index - 1:
      try:
        next_line = coordinates[idx+path[1]]
      except IndexError: 
        break
      x_axis_pos+=path[0]

      if next_line[x_axis_pos % max_len] == '#':
        counter+=1
      
      idx+=path[1]
    
    total*=counter

  print("Number of trees hit: {}".format(total))


def part_1(coordinates):
  max_len = len(coordinates[0])

  path = [3, 1]


  idx = 0
  x_axis_pos = 0
  last_index = len(coordinates)

  counter = 0

  while idx < last_index - 1:
    next_line = coordinates[idx+path[1]]
    
    x_axis_pos+=path[0]

    if next_line[x_axis_pos % max_len] == '#':
      counter+=1
    
    idx+=1

  print("Number of trees hit: {}".format(counter))


if __name__ == "__main__":
  with open('input.txt', 'r') as f: # Read in the data as a list of ints
    coordinates = [i for i in f.read().splitlines()]

  part_1(coordinates)
  part_2(coordinates)
