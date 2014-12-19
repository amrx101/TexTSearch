class Node:
	def __init__(self,letter):
		self.letter = letter
		self.isTerminal = False
		self.children = {}
		self.positions = []
