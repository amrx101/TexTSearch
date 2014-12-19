class Trie:
	def __init__(self):
		self.root = Node('')

	def __contains__(self, word):
		current = self.root
		for letter in word:
			if letter not in current.children:
				return False
			current = current.children[letter]
		return current.isTerminal

	def __getitem__(self, word):
		current = self.root
		for letter in word:
			if letter not in current.children:
				current.children[letter] = Node(letter)
			current = current.children[letter]
		current.isTerminal = True
		return current.positions

	def __str__(self):
		self.output([self.root])
		return ''

	def output(self, currentPath, indent=''):
		currentNode = currentPath[-1]
		if currentNode.isTerminal:
			word = ''.join(node.letter for node in currentPath)
			print indent+word+' '+str(currentNode.positions)
			indent += ' '
		for letter, node in sorted(currentNode.children.items()):
			self.output(currentPath[:]+[node],indent)
			
