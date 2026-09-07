class Trie:

    def __init__(self, is_end = False):
        self.end = is_end
        self.next = {}

    def insert(self, word: str) -> None:
        node = self
        for i, step in enumerate(word):
            if step in node.next:
                if i == len(word) - 1:
                    node.next[step] = Trie(True)
                    return
                node = node.next[step]
            else:
                if i == len(word) - 1:
                    node.next[step] = Trie(True)
                    node = node.next[step]
                else:
                    node.next[step] = Trie(False)
                    node = node.next[step]


    def search(self, word: str) -> bool:
        node = self
        for i, step in enumerate(word):
            if step in node.next:
                node = node.next[step]
                if i == len(word) -1:
                    if node.end != True:
                        return False
            else:
                return False
        return True
        

    def startsWith(self, prefix: str) -> bool:
        node = self
        for i, step in enumerate(prefix):
            if step in node.next:
                node = node.next[step]
            else:
                return False
        return True
        

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)