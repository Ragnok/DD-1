#!/usr/bin/python3
import random

class Dungeon:
	def __init__(self):
		rm_num = self.room
	def print_room(rm_num):
		if rm_num == 1:
			print ("┌─────────────────────────────────────────────────────────────────────────┐")
			print ("│Entrance to the Mine Shaft                                               │")
			print ("│  As you enter the mine shaft, you get a sudden fear of the walls closing│")
			print ("│in on you.  You are surprised to notice that you don't need a light.     │")
			print ("└─────────────────────────────────────────────────────────────────────────┘\n")
		if rm_num == 2:
			print ("┌─────────────────────────────────────────────────────────────────────────┐")
			print ("│  This mine shaft looks stable, at least in this area.  The wooden       │")
			print ("│supports are thick and strong.  Torches line the walls.                  │")
			print ("│Exits lead in all directions.                                            │")
			print ("└─────────────────────────────────────────────────────────────────────────┘\n")
		elif rm_num == 3:
			print ("┌─────────────────────────────────────────────────────────────────────────┐")
			print ("│  You enter a part of the mine shaft where the torches have grown dim    │")
			print ("│and are almost ready to go out.  From what you can see, there are plenty │")
			print ("│of cobwebs on the walls and rats at your feet.                           │")
			print ("└─────────────────────────────────────────────────────────────────────────┘\n")
		elif rm_num == 4:
			print ("┌─────────────────────────────────────────────────────────────────────────┐")
			print ("│  The floor dips slightly as you walk into this dark and nasty place.    │")
			print ("│Your skin crawls as you look at the filth on the walls and see it move.  │")
			print ("│Most of the exits lead into jail cells.                                  │")
			print ("└─────────────────────────────────────────────────────────────────────────┘\n")
		elif rm_num == 5:
			print ("┌─────────────────────────────────────────────────────────────────────────┐")
			print ("│  You are in the deepest and darkest part of the mine shafts.  The light │")
			print ("│from the torches barely reaches to where you are.  Most directions from  │")
			print ("│here lead to jail cells.                                                 │")
			print ("└─────────────────────────────────────────────────────────────────────────┘\n")
		elif rm_num == 6:
			print ("┌─────────────────────────────────────────────────────────────────────────┐")
			print ("│  You are inside a well guarded room.  The place is slightly better built│")
			print ("│than the mine shafts, and is lit by lanterns.                            │")
			print ("└─────────────────────────────────────────────────────────────────────────┘\n")
		elif rm_num == 7:
			print ("┌─────────────────────────────────────────────────────────────────────────┐")
			print ("│  The guards store their spare weapons and armor here.  There are rusty  │")
			print ("│swords on rotting shelves, and armor is laying on the floor.             │")
			print ("└─────────────────────────────────────────────────────────────────────────┘\n")
		elif rm_num == 8:
			print ("┌─────────────────────────────────────────────────────────────────────────┐")
			print ("│  You are on a well built path in the middle of a mountain.  You sense   │")
			print ("│something great up ahead, considering the hard work that must have gone  │")
			print ("│into creating this passage.                                              │")
			print ("└─────────────────────────────────────────────────────────────────────────┘\n")
		elif rm_num == 9:
			print ("┌─────────────────────────────────────────────────────────────────────────┐")
			print ("│  You have stepped into the Grand Hall of the kingdom; your luck         │")
			print ("│must be running low by now.  Golden pillars span the hallway, and you    │")
			print ("│notice a red carpet beneath your feet.                                   │")
			print ("└─────────────────────────────────────────────────────────────────────────┘\n")
		elif rm_num == 10:
			print ("┌─────────────────────────────────────────────────────────────────────────┐")
			print ("│  This is a large bright room filled with a strange monster.  Explore to │")
			print ("│the next room and you become the ruler and master of this realm!         │")
			print ("└─────────────────────────────────────────────────────────────────────────┘\n")
		else:
				#ASCII ART GENERATOR found http://patorjk.com/blog/software/
			print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
			print (" ██╗   ██╗ ██████╗ ██╗   ██╗      ")
			print (" ╚██╗ ██╔╝██╔═══██╗██║   ██║      ")
			print ("  ╚████╔╝ ██║   ██║██║   ██║      ")
			print ("   ╚██╔╝  ██║   ██║██║   ██║      ")
			print ("    ██║   ╚██████╔╝╚██████╔╝      ")
			print ("    ╚═╝    ╚═════╝  ╚═════╝       ")
			print ("                                  ")
			print (" ██╗    ██╗██╗███╗   ██╗██╗██╗██╗ ")
			print (" ██║    ██║██║████╗  ██║██║██║██║ ")
			print (" ██║ █╗ ██║██║██╔██╗ ██║██║██║██║ ")
			print (" ██║███╗██║██║██║╚██╗██║╚═╝╚═╝╚═╝ ")
			print (" ╚███╔███╔╝██║██║ ╚████║██╗██╗██╗ ")
			print ("  ╚══╝╚══╝ ╚═╝╚═╝  ╚═══╝╚═╝╚═╝╚═╝ ")
			print (" Congratulations you beat Dungeon Dudes!! ")
			print (" by MSG Mike Simpson")

