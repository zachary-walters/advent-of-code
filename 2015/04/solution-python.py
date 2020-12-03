#!/usr/bin/env python3
from hashlib import md5


def part_2(md5_hash_part):
  for i in range(10000000000):
    md5_hash = md5(bytes("{}{}".format(md5_hash_part, i), "ascii"))

    hex_digest = md5_hash.hexdigest()[0:6]

    if hex_digest == '000000':
      print("Lowest number: {}".format(i))
      break
  else:
    print("Not found, raise range.")


def part_1(md5_hash_part):
  for i in range(10000000000):
    md5_hash = md5(bytes("{}{}".format(md5_hash_part, i), "ascii"))

    hex_digest = md5_hash.hexdigest()[0:5]

    if hex_digest == '00000':
      print("Lowest number: {}".format(i))
      break
  else:
    print("Not found, raise range.")


if __name__ == "__main__":
  with open('input.txt', 'r') as f: # Read in the data as a list of ints
    md5_hash_part = f.read()

  part_1(md5_hash_part)
  part_2(md5_hash_part)  
