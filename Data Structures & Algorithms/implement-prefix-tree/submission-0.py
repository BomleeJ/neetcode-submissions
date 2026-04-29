class TrieNode:
    def __init__(self, letter = "", is_word=False):
        self.letter = letter
        self.is_word = is_word
        self.chars = {}

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        if word:
            node = self.root
            for char in word:
                if not node.chars.get(char):
                    node.chars[char] = TrieNode(char)
                node = node.chars.get(char)
            node.is_word = True



    def search(self, word: str) -> bool:
        node = self.root

        for char in word:
            if char in node.chars.keys():
                node = node.chars[char]
            else:
                return False
        
        return node.is_word

    def startsWith(self, prefix: str) -> bool:
        node = self.root

        for char in prefix:
            if char in node.chars.keys():
                node = node.chars[char]
            else:
                return False

        return True
        
        