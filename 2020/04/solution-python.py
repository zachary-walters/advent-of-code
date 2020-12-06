#!/usr/bin/env python3


import re
        

def part_2(passports):
  counter = 0

  valid_map = {
    'byr': r'^(19[2-8][0-9]|199[0-9]|200[0-2])$',
    'iyr': r'^(201[0-9]|2020)$',
    'eyr': r'^(202[0-9]|2030)$',
    'hgt': r'^((1[5-8][0-9]|19[0-3])cm|(59|6[0-9]|7[0-6])in)$',
    'hcl': r'^(#[0-9a-f]{6})$',
    'ecl': r'^(amb|brn|blu|gry|grn|hzl|oth)$',
    'pid': r'^([0-9]{9})$',
    'cid': r'^(cid:.*)$'
  }

  for passport in passports:
    fields = [f for f in passport.split(' ')]

    valid = 0
    cid = False
    for f in fields:
      if not f:
        continue

      value = f.split(':')[1]
      if re.match(valid_map.get('byr'), value):
        valid+=1
      elif re.match(valid_map.get('iyr'), value):
        valid+=1
      elif re.match(valid_map.get('eyr'), value):
        valid+=1
      elif re.match(valid_map.get('hgt'), value):
        valid+=1
      elif re.match(valid_map.get('hcl'), value):
        valid+=1
      elif re.match(valid_map.get('ecl'), value):
        valid+=1
      elif re.match(valid_map.get('pid'), value):
        valid+=1
      elif f.split(':')[0]:
        cid = True
        valid+=1

    if (valid == 7 and not cid) or (cid and valid == 8):
      counter+=1
  
  print(counter)



def part_1(passports):  
  counter = 0
  for passport in passports:
    fields = [f.split(':')[0] for f in passport.split(' ')]
    while 'cid' in fields: fields.remove('cid')
    if len(fields) == 7:
      counter+=1
  
  print(counter)



if __name__ == "__main__":
  passports = [[]]
  with open('input.txt', 'r') as f: 
    lines = [i for i in f.read().splitlines()]

  pass_count = 0
  passports.append([])
  for idx, line in enumerate(lines):
    if line:
      passports[pass_count].append(line)
    else:
      pass_count+=1
      passports.append([])

  for idx, each in enumerate(passports):
    passports[idx] = ' '.join(each)

  part_1(passports)
  part_2(passports)