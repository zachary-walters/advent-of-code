#!/usr/bin/env python3


def part_1(target, numbers): # Find the 2 numbers that compliment to the target
  for num in numbers:
    compliment = target - num
    if compliment in numbers:
      print("Part 1 Answer {} * {} = {}".format(num, compliment, num * compliment))
      break
  else:
    exit("refactor code. No matches found.")


def part_2(target, numbers): # Find the 3 numbers that sum to the target
  numbers.sort()
  found = False

  for idx, _ in enumerate(numbers):
    next_idx = idx + 1
    last_idx = len(numbers) - 1

    while last_idx >= next_idx:
      summation = numbers[idx] + numbers[next_idx] + numbers[last_idx]

      if summation == target:
        print("Part 2 Answer {} * {} * {} = {}".format(numbers[idx],
                                                       numbers[next_idx], 
                                                       numbers[last_idx], 
                                                       numbers[idx] * numbers[next_idx] * numbers[last_idx]))
        found = True
        break

      if summation > target:
        last_idx-=1
      else:
        next_idx+=1
    
    if found:
      break
  else:
    exit("refactor code. No matches found.")


if __name__ == '__main__':
  target = 2020

  numbers = []
  with open('input.txt', 'r') as f: # Read in the data as a list of ints
    numbers = [int(i) for i in f.read().splitlines()]

  part_1(target, numbers)
  part_2(target, numbers)
