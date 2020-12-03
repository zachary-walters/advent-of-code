#!/usr/bin/env python3


def part_2(directions):
  x = 0
  y = 0
  i = 0
  j = 0

  coordinates_s = {(x, y)}
  coordinates_r = {(i, j)}

  for idx, direction in enumerate(directions):
    if idx % 2 == 0:
      if direction == '>':
        x+=1
      elif direction == '^':
        y+=1
      elif direction == '<':
        x-=1
      else:
        y-=1

      coordinates_s.add((x, y))
    else:
      if direction == '>':
        i+=1
      elif direction == '^':
        j+=1
      elif direction == '<':
        i-=1
      else:
        j-=1
      
      coordinates_r.add((i, j))

  print(len(coordinates_r.union(coordinates_s)))


def part_1(directions):
  x = 0
  y = 0

  coordinates = {(x, y)}

  for direction in directions:
    if direction == '>':
      x+=1
    elif direction == '^':
      y+=1
    elif direction == '<':
      x-=1
    else:
      y-=1

    coordinates.add((x, y))

  print(len(coordinates))


if __name__ == "__main__":
  directions = []
  with open('input.txt', 'r') as f: # Read in the data as a list of ints
    directions = f.read()

  part_1(directions)
  part_2(directions)  
