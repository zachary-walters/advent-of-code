#!/usr/bin/env python3


def part_2(dimensions):
  total_sq_ft = 0
  for dimension in dimensions:
    h = int(dimension.split('x')[0])
    w = int(dimension.split('x')[1])
    l = int(dimension.split('x')[2])

    bow = h * w * l

    tie = [h, w, l]

    tie.remove(max(tie))

    total_sq_ft = total_sq_ft + bow + tie[0] * 2 + tie[1] * 2
  
  print(total_sq_ft)


def part_1(dimensions):
  total_sq_ft = 0
  for dimension in dimensions:
    h = int(dimension.split('x')[0])
    w = int(dimension.split('x')[1])
    l = int(dimension.split('x')[2])

    area = 2 * l * w + 2 * w * h + 2 * h * l

    dims = [h, w, l]

    dims.remove(max(dims))

    total_sq_ft = total_sq_ft + area + dims[0] * dims[1]
  
  print(total_sq_ft)


if __name__ == "__main__":
  dimensions = []
  with open('input.txt', 'r') as f: # Read in the data as a list of ints
    dimensions = [i for i in f.read().splitlines()]

  part_1(dimensions)
  part_2(dimensions)
