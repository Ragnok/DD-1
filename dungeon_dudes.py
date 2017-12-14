#!/usr/bin/python3
import random
from dungeon import Dungeon
from dice import Dice
from character import *


def main():

	Commands = {'explore': Player.explore,'E': Player.explore,'status': Player.status,
		'S': Player.status,'attack': Player.attack,'A': Player.attack,'rest': Player.rest,'R': Player.rest,
		'flee': Player.flee,'F': Player.flee,'quit': Player.quit,'Q': Player.quit,'help': Player.help,
		'look':Player.look,'L':Player.look,'I':Player.gold,'inventory':Player.gold,'H': Player.help,
		'M':Player.monster_health,'monster':Player.monster_health}

	#main
	p = Player()
	m = Monster(p)
	#ASCII ART GENERATOR found http://patorjk.com/blog/software/
	print (" ________                                             ")
	print (" \______ \  __ __  ____    ____   ____  ____   ____   ")
	print ("  |    |  \|  |  \/    \  / ___\_/ __ \/  _ \ /    \  ")
	print ("  |    `   \  |  /   |  \/ /_/  >  ___(  <_> )   |  \ ")
	print (" /_______  /____/|___|  /\___  / \___  >____/|___|  / ")
	print ("         \/           \//_____/      \/           \/  ")
	print (" ")
	print (" ")
	print ("  _ .-') _               _ .-') _     ('-.    .-')    ")
	print (" ( (  OO) )             ( (  OO) )  _(  OO)  ( OO ).  ")
	print ("  \     .'_  ,--. ,--.   \     .'_ (,------.(_)---\_) ")
	print (" ,`'--..._) |  | |  |   ,`'--..._) |  .---'/    _ |   ")
	print (" |  |  \  ' |  | | .-') |  |  \  ' |  |    \  :` `.   ")
	print (" |  |   ' | |  |_|( OO )|  |   ' |(|  '--.  '..`''.)  ")
	print (" |  |   / : |  | | `-' /|  |   / : |  .--' .-._)   \  ")
	print (" |  '--'  /('  '-'(_.-' |  '--'  / |  `---.\       /  ")
	print ("  `-------'   `-----'    `-------'  `------' `-----'  ") 
 
	p.name = input("Enter your name? ")
	print ("(type help to get this list of actions)\n")
	print ("┌─────────────────────────────────────────────────────────────────────────┐")
	print ("│Entrance to the Mine Shaft                                               │")
	print ("│  As you enter the mine shaft, you get a sudden fear of the walls closing│")
	print ("│in on you.  You are surprised to notice that you don't need a light.     │")
	print ("└─────────────────────────────────────────────────────────────────────────┘\n")
	max_rooms = 100
	while(p.health > 0 and p.room < max_rooms):
		num = p.health
		print ("%s Health:" % p.name)
		for num in range(num):
			print ("█",end="",flush=True)
		line = input("\n> ")
		args = line.split()
		if len(args) > 0:
			commandFound = False
			for c in Commands.keys():
				if args[0] == c[:len(args[0])]:
					Commands[c](p)
					commandFound = True
					break
			if not commandFound:
				print ("%s.. please type help for availible commands" % p.name)

if __name__ == "__main__":
    main()

