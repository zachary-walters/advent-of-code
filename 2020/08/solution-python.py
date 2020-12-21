#!/usr/bin/env python3


def part_2(instructions):
  index = 0
  accumulator = 0
  change_list = []
  index_list = []
  new_instructions = list(instructions)
  duped = False

  for idx, instruction in enumerate(instructions):
    if instruction.split(' ')[0] == 'jmp':
      change_list.append(idx)

  for idx, instruction in enumerate(instructions):
    if instruction.split(' ')[0] == 'nop':
      change_list.append(idx)

  while index < len(new_instructions):
    if index in index_list:
      duped = True

    if duped:
      duped = False
      index_list = []
      index = 0
      accumulator = 0
      new_instructions = list(instructions)
      change = change_list[0]
      change_list.pop(0)
      inst_func = instructions[change].split(' ')[1]
      new_instructions[change] = 'nop {}'.format(inst_func) if instructions[change].split(' ')[0] == 'jmp' else 'jmp {}'.format(inst_func)

      continue
    
    index_list.append(index)
    
    inst_type = new_instructions[index].split(' ')[0]
    inst_func = new_instructions[index].split(' ')[1]


    if inst_type == 'acc':
      accumulator+=int(inst_func)
      index+=1
    elif inst_type == 'jmp':
      index+=int(inst_func)
    else:
      index+=1

  print(accumulator)


def part_1(instructions): 

  index = 0
  accumulator = 0
  index_list = []
  
  while True:
    if index in index_list:
      print("Accumulator: {}".format(accumulator))
      break

    index_list.append(index)

    inst_type = instructions[index].split(' ')[0]
    inst_func = instructions[index].split(' ')[1]

    if inst_type == 'acc':
      accumulator+=int(inst_func)
      index+=1
    elif inst_type == 'jmp':
      index+=int(inst_func)
    else:
      index+=1


if __name__ == "__main__":
  with open('input.txt', 'r') as f: 
    instructions = [i for i in f.read().splitlines()]
      
  part_1(instructions)
  part_2(instructions)
