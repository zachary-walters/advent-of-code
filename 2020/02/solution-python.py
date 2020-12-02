#!/usr/bin/env python3

import re


def part_1(password_reqs):
  counter = 0
  for req in password_reqs:
    min_num = int(req.split('-')[0])
    max_num = int(req.split('-')[1].split(' ')[0])
    letter = req.split(' ')[1].replace(':', '')
    password = req.split(':')[1].strip()

    num_of_letter = password.count(letter)

    if num_of_letter >= min_num and num_of_letter <= max_num:
      counter+=1

  print("Amount of valid passwords: {} out of {}.".format(counter, len(password_reqs)))


def part_2(password_reqs):
  counter = 0

  for req in password_reqs:
    f_char_index = int(req.split('-')[0]) - 1
    l_char_index = int(req.split('-')[1].split(' ')[0]) - 1
    letter = req.split(' ')[1].replace(':', '')
    password = req.split(':')[1].strip()

    if len(password) < l_char_index: # gracefully check the password length to avoid out of bounds exceptions
      continue

    if (password[f_char_index] == letter) != (password[l_char_index] == letter): 
      counter+=1
      


  print("Amount of valid passwords: {} out of {}.".format(counter, len(password_reqs)))


if __name__ == '__main__':
  password_reqs = []
  with open('input.txt', 'r') as f: # Read in the data as a list of ints
    password_reqs = [i for i in f.read().splitlines()]

  part_1(password_reqs)
  part_2(password_reqs)