#!/usr/bin/env python3


def part_1(directions):
  position = 0
  face = 0 

  coord = [
    {'L': -1, 'R': 1},      # 0 North
    {'L': -1, 'R': 1},      # 1 East
    {'L': 1, 'R': -1},      # 2 South
    {'L': 1, 'R': -1}       # 3 West
  ]
  rotation = {'R': 1, 'L': -1}

  face = 0 
  horizontal = 0
  vertical = 0

  for token in directions:
    move = token[0]
    sign = coord[face][move]

    if face % 2 == 0:
      horizontal += sign * int(token[1:])
    else:
      vertical += sign * int(token[1:])
    face = (face + 4 + rotation[move]) % 4

  print("Distance from the start: {}".format(abs(vertical) + abs(horizontal)))


if __name__ == '__main__':
  with open('input.txt', 'r') as f: # Read in the data as a list of ints
    directions = [i.strip() for i in f.read().split(',')]

  part_1(directions)

  