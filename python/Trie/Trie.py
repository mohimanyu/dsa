class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root

        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]

        curr.is_end = True

    def search(self, word: str) -> bool:
        curr = self.root

        if not curr:
            return False
        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]

        return curr.is_end

    def startsWith(self, prefix: str) -> bool:
        curr = self.root

        if not curr:
            return False
        for char in prefix:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return True

    def delete(self, word):
        def _delete(node, word, index):
            if index == len(word):
                if not node.is_end:
                    return False
                node.is_end = False
                return len(node.children) == 0

            char = word[index]
            if char not in node.children:
                return False

            should_delete = _delete(node.children[char], word, index + 1)

            if should_delete:
                del node.children[char]
                return len(node.children) == 0 and not node.is_end

            return False

        return _delete(self.root, word, 0)

    def allWordsWithPrefix(self, prefix):
        def dfs(node, path, result):
            if node.is_end:
                result.append("".join(path))
            for char, nxt in node.children.items():
                dfs(nxt, path + [char], result)

        curr = self.root
        for char in prefix:
            if char not in curr.children:
                return []
            curr = curr.children[char]

        result = []
        dfs(curr, list(prefix), result)
        return result


trie = Trie()

trie.insert("apple")
trie.insert("app")
trie.insert("bat")
trie.insert("ball")

print(trie.search("apple"))  # True
print(trie.search("appl"))  # False
print(trie.startsWith("app"))  # True
print(trie.startsWith("ba"))  # True
print(trie.startsWith("cat"))  # False
# print(trie.delete("apple"))  # True
print(trie.allWordsWithPrefix("app"))  # ['apple', 'app']
