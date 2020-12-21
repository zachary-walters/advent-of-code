#!/usr/bin/env python3


def part_1(jolts): 
  jolts = [int(i) for i in jolts]
  jolts.sort()

  one_jolt_diff = 1 # this accounts for the first plug used
  three_jolt_diff = 1 # this accounts for the 3 jolt higher rating

  for idx in range(len(jolts) - 1):
    if jolts[idx+1] - jolts[idx] == 1:
      one_jolt_diff+=1
    elif jolts[idx+1] - jolts[idx] == 3:
      three_jolt_diff+=1

  print(one_jolt_diff * three_jolt_diff)


if __name__ == "__main__":
  with open('input.txt', 'r') as f: 
    jolts = [i for i in f.read().splitlines()]
      
  part_1(jolts)
