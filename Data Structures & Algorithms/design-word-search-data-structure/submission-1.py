class TrieNode:
    def __init__(self):
        self.nextChars = {}
        self.is_word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root

        for char in word:
            if not node.nextChars.get(char):
                node.nextChars[char] = TrieNode()
            node = node.nextChars[char]
        node.is_word = True

    def searchbyIdx(self, word, index, node):
        for idx in range(index, len(word)):
            c = word[idx]

            if c == ".":
                for node in node.nextChars.values():
                    if self.searchbyIdx(word, idx + 1, node):
                        return True
                return False
            elif c in node.nextChars.keys():
                node = node.nextChars[c]
            else:
                return False
        
        return node.is_word
        
    def search(self, word: str) -> bool:
       return self.searchbyIdx(word, 0, self.root)
