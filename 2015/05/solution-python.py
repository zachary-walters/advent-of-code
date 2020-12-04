#!/usr/bin/env python3


def part_2(strings):
  counter = 0

  for s in strings:
    idx = 0
    cond_0 = False 
    cond_1 = False

    while idx < len(s) - 1:
      if idx+2 < len(s) and s[idx] == s[idx+2] and s[idx] != s[idx+1] and cond_1 is False:
        cond_1 = True

      if idx+1 < len(s) and s.count(s[idx]+s[idx+1]) >= 2 and cond_0 is False:
        cond_0 = True

      if cond_0 and cond_1:
        counter+=1
        break

      idx+=1 

  print(counter)


def part_1(strings):  
  bad_strings = ['ab','cd','pq','xy']
  vowels = ['a', 'e', 'i', 'o', 'u']
  counter = 0

  for s in strings:
    cond_0 = False
    cond_1 = False

    vowel_count = 0

    for b in bad_strings:
      if b in s:
        cond_1 = True
        break 

    if cond_1:
      continue

    for idx, _ in enumerate(s):
      if s[idx] in vowels:
        vowel_count+=1

    for idx, _ in enumerate(s[:-1]):
      if s[idx] == s[idx+1]:
        cond_0 = True

      if vowel_count > 2 and cond_0:
        counter+=1
        break 

  print("Nice Strings: {}".format(counter))


if __name__ == "__main__":
  with open('input.txt', 'r') as f: # Read in the data as a list of ints
    strings = [i for i in f.read().splitlines()]

  part_1(strings)
  part_2(strings)
