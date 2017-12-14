#!/usr/bin/python3
import random
from dungeon import Dungeon
from dice import Dice
		
class Character:
	def __init__(self):
		self.name = ""
		self.health = 0
		self.health_max = 0
		self._dice = []
	def roll(self):
		list1 = []
		for item in self._dice:
			list1.append(item.roll())
		return list1
	def do_damage(self, monster):
		damage = 1
		monster.health = monster.health - damage
		print ("%s hurts %s!" % (self.name, monster.name))
		return monster.health <= 0

	def help(self): 
		print (" Type the entire command or character: look or l or L")
		print (" (E)xplore 	 move forward in your quest")
		print (" (S)tatus  	 shows your currnt health")
		print (" (M)onster 	 show Monster health status")
		print (" (L)ook 	 look around room")
		print (" (A)ttack 	 attack the monster in the room")
		print (" (R)est  	 if uninterupted you will regenerate 1 -5 hit points")
		print (" (F)lee 	 if successful you will escape the current battle")
		print (" (I)nventory 	 shows how much coin you have collected")
		print (" (Q)uit 	 quit and end your adventures")
		print (" ")
		print (" help		 displays availible comannds and descriptions\n")
#		print (Commands.keys())

	def quit(self):
		print ("Thank you for playing %s!!\n" % self.name)
		self.health = 0


class Monster(Character):
	def __init__(self, player):
		super().__init__()
		Character.__init__(self)
		
		all_monsters = ['a Banshee', 'the Bogeyman', 'a Chimera', 'a large Cyclopse',
		'a Red Dragon', 'a Demon', 'a Gorgon', 'a Hydra', 'a Hobgoblin', 'an Imp',
		'a Mermaid', 'a Nymph', 'a Sprite', 'a Unicorn', 'a Vampire', 'a Zombie',
		'a Werewolf', 'a Wraith', 'a Sphinx', 'a Shade', 'an Ogre', 'a Minotaur']
		monster = random.choice(all_monsters)
#		print monster
		self.name = monster
		self.health_max = random.randint(1, 3)
		self.health = self.health_max
		if self.health ==1:
			self._dice=[Dice(6)]
		if self.health ==2:
			self._dice=[Dice(6),Dice(6)]
		else:
			self._dice=[Dice(6),Dice(6),Dice(6)]

	def initiative(self):
		dice1 = random.randint(0,6)
		return dice1

class Player(Character):
	def __init__(self):
		super().__init__()
		self.state = 'peace'
		self.health = 10
		self.health_max = 10
		self.room = 1
		self.gold = 0
		self.monster = None
		self._dice=[Dice(6),Dice(6),Dice(6)]
	def initiative(self):
		dice1 = random.randint(0,6)
		return dice1
	
	def gold(self):
		print ("%s has treasure in the amount of %d gold coins!" % (self.name, self.gold))
		
	def status(self): 
		print ("%s's health: %d/%d" % (self.name, self.health, self.health_max))

	def monster_health(self):
		if (self.monster): 
			print ("%s's health: %d/%d" % (self.monster.name, self.monster.health, self.monster.health_max))
		else:
			print ("%s you are currently not in combat!" % self.name)
			
	def tired(self):
		print ("%s feels tired." % self.name)
		self.health = max(1, self.health - 1)

	def look(self):
		room = self.room
		if (room ==1):
			print ("┌─────────────────────────────────────────────────────────────────────────┐")
			print ("│Entrance to the Mine Shaft                                               │")
			print ("│  As you enter the mine shaft, you get a sudden fear of the walls closing│")
			print ("│in on you.  You are surprised to notice that you don't need a light.     │")
			print ("└─────────────────────────────────────────────────────────────────────────┘\n")
		else:
			Dungeon.print_room(self.room)

	def rest(self):
		if (self.state == 'peace'):#cant rest in a fight
			print ("%s sits down and rests." % self.name)
			if random.randint(0, 1):#50/50 he will rest and get hp back
				self.monster = Monster(self)#Create monster
				print ("%s resting is interupted by %s!" % (self.name, self.monster.name))
				self.state = 'fight'
				self.monster_attacks()
			else:
				if (self.health < self.health_max):
					if ((self.health + 5) > self.health_max):#cant go over health_max
						self.health = self.health_max
					else:
						self.health = self.health + 5
				else: 
					print ("%s is fully healed." % self.name)
		else:
			print("Can not rest in combat!")
			
	def explore(self):
		self.room += 1#count hero's rooms
		if self.state != 'peace':
			print ("%s is too busy right now!" % self.name)
			self.monster_attacks()
		else:
#			print ("%s explores." % self.name)
			Dungeon.print_room(self.room)
			if self.room > 10:
				self.room = 100;
			num = 1	
			if (self.room<11):#100% chance of monster
				self.monster = Monster(self)#create monster
				if (self.initiative() >= self.monster.initiative()):
					self.state = 'fight'
					print ("%s sees %s looking for prey!" % (self.name, self.monster.name))
				else:
					self.state = 'fight'
					print ("%s sees you and attacks!" % (self.monster.name))
					self.monster_attacks()
				
	def flee(self):
		if (self.state == 'fight'):
			if random.randint(1, self.health) > random.randint(1, self.monster.health):
				print ("%s flees from %s." % (self.name, self.monster.name))
				self.monster = None
				self.state = 'peace'
			else: 
				print ("%s couldn't escape from %s!" % (self.name, self.monster.name))
				self.monster_attacks()
		else:
			print("%s runs around in a panic..  you are alone" % (self.name))
			
	def attack(self):
		if (self.monster!=None):
			num = self.monster.health
			for num in range(num):
				print ("█",end="",flush=True)
			print ("")

			if (max(self.roll()))>=(max(self.monster.roll())):
				if self.do_damage(self.monster)==1:#check if monster dead
					gold = random.randint(1,25)
					print ("        ___										")
					print ("      .'   `.									")
					print ("      | RIP |   %s is no more " % (self.monster.name))
					print ("      |     |									")
					print ("    \\\\|     |//								")
					print (" ^^^^^^^^^^^^^^^^^						")                           
					print ("%s collects %d gold from the corpse of %s!" % (self.name, gold, self.monster.name))
					self.gold += gold
					self.monster = None
					self.state = 'peace'
			else:
				print ("%s misses!"% self.name)
			if (self.monster!=None):
				if(max(self.monster.roll()))>=(max(self.roll())): 
					if self.monster.do_damage(self)==1:#check if player dead 
						print ("%s was slain by %s!\n" %(self.name, self.monster.name))
						print ("")
						print ("HINT: Remember to watch your health (S) and rest (R) when you can!\nGAME OVER")
				else:
					print ("%s misses!"% self.monster.name)
		else:
			print ("You inspect the room for a creature to attack.. you are alone..")
				
	def monster_attacks(self):
		if (self.monster.name!=None):
			num = self.monster.health
			for num in range(num):
				print ("█",end="",flush=True)
			print ("")
			
			if (max(self.monster.roll()))>=(max(self.roll())):
				if self.monster.do_damage(self)==1:#check if player dead 
					print ("%s was slain by %s!\n" %(self.name, self.monster.name))
					print ("")
					print ("HINT: Remember to watch your health (S) and rest (R) when you can!\nGAME OVER")
			else:
				print ("%s misses!"% self.monster.name)

			if (max(self.roll()))>=(max(self.monster.roll())):
				if self.do_damage(self.monster)==1:#check if monster dead
					gold = random.randint(1,25)
					print ("        ___										")
					print ("      .'   `.									")
					print ("      | RIP |   %s is no more " % (self.monster.name))
					print ("      |     |									")
					print ("    \\\\|     |//							")
					print (" ^^^^^^^^^^^^^^^^^						")                           
					print ("%s collects %d gold from the corpse of %s!" % (self.name, gold, self.monster.name))
					self.gold += gold
					self.monster = None
					self.state = 'peace'
			else:
				print ("%s misses!"% self.name)


