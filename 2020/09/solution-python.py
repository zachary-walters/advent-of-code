#!/usr/bin/env python3


def part_2(preamble, invalid_number):
  preamble = [int(i) for i in preamble]
  filter_list = []

  index = 0 
  while index < len(preamble):
    val_sum = sum(filter_list)
    
    if len(filter_list) >=2 and val_sum == invalid_number:
      print('Encryption Weakness: {}'.format(min(filter_list) + max(filter_list)))
      break
    elif val_sum < invalid_number:
      filter_list.append(preamble[index])
      index+=1
    else:
      filter_list.pop(0)


def part_1(preamble): 
  preamble = [int(i) for i in preamble]
  filter_list = list(preamble[:25])
  preamble = list(preamble[25:])

  for val in preamble:
    found = True
    filter_list.sort()
    start_idx = 0 
    end_idx = len(filter_list) - 1 

    while start_idx < end_idx:
      if filter_list[start_idx] + filter_list[end_idx] > val:
        end_idx-=1
      elif filter_list[start_idx] + filter_list[end_idx] == val:
        filter_list.append(val)
        found = False
        break
      else:
        start_idx+=1

    if found: 
      print("First value that doesn't add up: {}".format(val))
      return val
      

if __name__ == "__main__":
  with open('input.txt', 'r') as f: 
    preamble = [i for i in f.read().splitlines()]
      
  invalid_number = part_1(preamble)
  part_2(preamble, invalid_number)
