#!/usr/bin/env python3


def part_2(boarding_passes):
  passes = []

  for bpass in boarding_passes:
    row_logic = bpass[:7]
    col_logic = bpass[7:]

    rows = [i for i in range(128)]
    cols = [i for i in range(8)]

    for row_direction in row_logic:
      if row_direction == 'F':
        rows = rows[:int(len(rows) / 2)]
      else:
        rows = rows[int(len(rows) / 2):]

    for col_direction in col_logic:
      if col_direction == 'L':
        cols = cols[:int(len(cols) / 2)]
      else:
        cols = cols[int(len(cols) / 2):]

    passes.append(rows[0] * 8 + cols[0])

  passes.sort()
  for i in range(passes[-1]):
    if i not in passes and i >= passes[0]:
      print("My Seat ID is: {}".format(i))
      break
        

def part_1(boarding_passes):  
  seat_id = 0
  for bpass in boarding_passes:
    row_logic = bpass[:7]
    col_logic = bpass[7:]

    rows = [i for i in range(128)]
    cols = [i for i in range(8)]

    for row_direction in row_logic:
      if row_direction == 'F':
        rows = rows[:int(len(rows) / 2)]
      else:
        rows = rows[int(len(rows) / 2):]

    for col_direction in col_logic:
      if col_direction == 'L':
        cols = cols[:int(len(cols) / 2)]
      else:
        cols = cols[int(len(cols) / 2):]

    if rows[0] * 8 + cols[0] > seat_id:
        seat_id = rows[0] * 8 + cols[0]
    
  print("The Highest Seat ID: {}".format(seat_id))


if __name__ == "__main__":
  with open('input.txt', 'r') as f: 
    boarding_passes = [i for i in f.read().splitlines()]

  part_1(boarding_passes)
  part_2(boarding_passes)
