def createIndex(text):
	trie = Trie()
	words = getWords(text)
	for pos, word in enumerate(words):
		trie[word].append(pos)
	return trie

def queryIndex(index, word):
	if word in index:
		return index[word]
	else:
		return []
