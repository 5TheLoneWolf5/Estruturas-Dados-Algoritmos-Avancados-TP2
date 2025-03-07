"""

Resultado:



Comparação de desempenho:



"""

class Grafo:
    def __init__(self):
        self.lista_adjacencia = {}

    def adicionar_vertice(self, vertice):
        if vertice[1] not in self.lista_adjacencia:
            self.lista_adjacencia[vertice] = []

    def adicionar_aresta(self, vertice1, vertice2):
        if vertice1 in self.lista_adjacencia and vertice2 in self.lista_adjacencia:
            self.lista_adjacencia[vertice1].append(vertice2)
            self.lista_adjacencia[vertice2].append(vertice1)
            
    def mostrar_grafo(self):
        for vertice in self.lista_adjacencia:
            print(f"{vertice[1]} -> {self.lista_adjacencia[vertice]}")

    def mostrar_vizinhos(self, vertice):
        if vertice in self.lista_adjacencia:
            print(f"Vizinhos de {vertice[1]}: {self.lista_adjacencia[vertice]}")
        else:
            print(f"O vértice {vertice[1]} não existe no grafo.")

    def bfs(self, vertice1, vertice2):
        visitados = set()
        fila = [vertice1]
 
        while fila:
            vertice = fila.pop(0)
            if vertice not in visitados:
                if 
                print(vertice, end=" ")
                visitados.add(vertice)
                fila.extend(self.lista_adjacencia[vertice])

grafo = Grafo()

centros = [(5, "A"), (4, "B"), (2, "C"), (6, "D"), (3, "E")]

for c in centros:
    grafo.adicionar_vertice(c)

arestas = [(centros[0], centros[1]), (centros[0], centros[2]), (centros[1], centros[3]), (centros[2], centros[4]), (centros[3], centros[4])]
for v1, v2 in arestas:
    grafo.adicionar_aresta(v1, v2)

print("Lista de Adjacência do Grafo:")
grafo.mostrar_grafo()

print("Lista de Vizinhos:")
for c in centros:
    grafo.mostrar_vizinhos(c)

print("Encontrando rota mais curta entre A e C com BFS: ")
grafo.bfs("A", "C")
