#!/usr/bin/env python3


def part_2(answer_persons_groups):  
  counter = 0
  for answer_group in answer_persons_groups:
    for answer_persons in answer_group:
      a = answer_persons[0]
      for answers in answer_persons:
        b = answers
        intersect = [val for val in a if val in b]
        a = intersect
      counter+=len(a)
  
  print("Number of questions where anyone said yes: {}".format(counter))


def part_1(answer_persons_groups):  
  counter = 0
  for answer_group in answer_persons_groups:
    for answer_persons in answer_group:
      
      char_set = set()
      for answers in answer_persons:
        char_set = char_set.union({c for c in answers})
      
      counter+=len(char_set)
  
  print("Number of questions where anyone said yes: {}".format(counter))


if __name__ == "__main__":
  with open('input.txt', 'r') as f: 
    answer_group_inputs = [i for i in f.read().splitlines()]

  answer_persons_groups = [[]] 
  group = []
  idx = 0
  for answer_group in answer_group_inputs:
    if not answer_group:
      idx+=1
      group = []
      answer_persons_groups.append([])
    else: 
      group.append(answer_group)
      answer_persons_groups[idx].clear()
      answer_persons_groups[idx].append(group)
      
  part_1(answer_persons_groups)
  part_2(answer_persons_groups)
