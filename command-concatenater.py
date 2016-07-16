#!/usr/bin/env python3
import skilstak.colors as c

def clear():
  print(c.clear,end='')

while True:
  clear()
  clearchoice = input(c.base3+ 'Welecome, this program will ask you for a list of commands and compile them into one command. It does this by spawning multiple Command Blocks on top of the Command Block you did the command in. When all of your commands are finnished, would you like to...\n\n'+c.red+'[1] Clear all Command Blocks (recommended).\n'+c.blue+'[2] Only clear the spawned Command Block(s).\n'+c.green+"[3] Only clear the original Command Block.\n"+c.yellow+"[4] Don't clear any command blocks.\n\n"+c.magenta+'Input your desired choice to continue.\n>>> ')
  if clearchoice == '':
    clearchoice = '1'
  if clearchoice == '1' or clearchoice == '2' or clearchoice == '3' or clearchoice == '4':
    break
    
commands = []
while True:
  clear()
  try:
    print()
    command_num = 0
    for pr_command in commands:
      command_num += 1
      print(c.green + 'Command #' + str(command_num) + ': ' + pr_command)
    print()
    command = input(c.base3 + "Now type your commands in the order you want them to be ran in. Hit Ctrl+D to undo your last command. Hit Ctrl+C when you have sent all of your commands.\n\n>>> /").strip()
    command = '/' + command
    if command != '/':
      commands.append(command)
    elif commmand.startswith('//'):
      command = command[1:]
  except KeyboardInterrupt:
    clear()
    break
  except EOFError:
    if commands != []:
      commands.pop()

master = '/summon FallingSand ~ ~1 ~ {Time:1,Block:command_block,TileEntityData:{auto:1,Command:"'

bracket_count = -1

for command in commands:
  master += command + '"},Passengers:[{id:FallingSand,Time:1,Block:command_block,TileEntityData:{auto:1,Command:"'
  bracket_count += 1

master = master[:-88]

for bracket in range(bracket_count):
  master += '}]'
master += '}'
print(master)