"""

Após inserir, estes valores na estrutura Trie:

['casa', 'carro', 'caminhão', 'cachorro', 'cadeira']

Esta é a representação de sua estrutura hierárquica:

                               root
                                 | 
                                 c
                                 |
                                 a
                               / |  \   \   \
                             s   r   m   c   d
                           /     |   |   |   | 
                          a      r   i   h   e
                                 |   |   |   |
                                 o   n   o   i
                                     |   |   |
                                     h   r   r
                                     |   |   |
                                     ã   r   a
                                     |   |
                                     o   o

Como é possível visualizar, a árvore Trie é n-ária, podendo ter n filhos. As aplicações dessa estrutura são diversas, e é uma solução eficiente para guardar e buscar textos.

"""

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True
    
    def delete(self, word):

        def _delete(node, word, depth): # Auxiliary.
            if depth == len(word):
                if not node.is_end_of_word:
                    return False
                node.is_end_of_word = False
                return len(node.children) == 0
            char = word[depth]

            if char not in node.children:
                return False

            should_delete_child = _delete(node.children[char], word, depth + 1)

            if should_delete_child:
                del node.children[char]
                return len(node.children) == 0 and not node.is_end_of_word
            
            return False
        
        _delete(self.root, word, 0)
            
    def list_words(self):
        
        def _dfs(node, prefix, words):
            if node.is_end_of_word:
                words.append(prefix)
            for char, child in node.children.items():
                _dfs(child, prefix + char, words)

        words = []
        _dfs(self.root, "", words)
        return words

    def displayUtil(self,visited,node,strin):
        index=0
        while index<26:
            if node.children[index]:
                strin+=char(97+index)
                #print(2,str)
                if node.children[index].isEndOfWord == False:
                    self.displayUtil(visited,node.children[index],strin)
                    strin=strin[0 : (len(strin)-1)]
                else:
                    if strin not in visited:
                        visited.append(strin)
                    if self.haschild(node.children[index]):
                        self.displayUtil(visited,node.children[index],strin)
                        strin=strin[0 : (len(strin)-1)]
                     
            index+=1

    def display(self):
        visited=[]
        strin=''
        self.displayUtil(visited,self.root,strin)
        print("Content of Trie:")
        for i in range(len(visited)):
            print(visited[i])

trie = Trie()
trie.insert("casa")
trie.insert("carro")
trie.insert("caminhão")
trie.insert("cachorro")
trie.insert("cadeira")

print(trie.list_words())
trie.display()
