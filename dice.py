#!/usr/bin/python3
import random

class Dice:
	def __init__(self, sides):
		self._sides = sides
	def roll(self):
		return random.randint(1,self._sides) 
