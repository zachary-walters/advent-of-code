#!/usr/bin/env python3


def part_2(parens):
  counter = 0
  for idx, p in enumerate(parens):
    if p == '(':
      counter+=1
    else: 
      counter-=1

    if counter == -1:
      print("First step into the basement: {}".format(idx + 1))
      break


def part_1(parens):
  counter = 0
  for p in parens:
    if p == '(':
      counter+=1

  steps = counter - (len(parens) - counter)

  print("Ending Floor: {}".format(steps))

if __name__ == "__main__":
  parens = []
  with open('input.txt', 'r') as f: # Read in the data as a list of ints
    parens = f.read()

part_1(parens)
part_2(parens)
