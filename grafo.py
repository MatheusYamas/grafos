from vertice import Vertice

class Grafo:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.vertices = [Vertice(i) for i in range(num_vertices)]

    def cria_adjacencia(self, i, j, P):
        if 0 <= i < self.num_vertices and 0 <= j < self.num_vertices:
            self.vertices[i].adicionar_adjacencia(j, P)
        else:
            print("Erro: Índices de vértices inválidos.")

    def remove_adjacencia(self, i, j):
        if 0 <= i < self.num_vertices:
            self.vertices[i].remover_adjacencia(j)

    def imprime_adjacencias(self):
        print("Matriz de Adjacências:")
        for i in range(self.num_vertices):
            linha_matriz = [0] * self.num_vertices
            for aresta in self.vertices[i].adjacencias:
                linha_matriz[aresta.destino] = aresta.peso
            
            rotulo = self.vertices[i].informacao
            linha_str = "\t".join(map(str, linha_matriz))
            print(f"{rotulo:<15} |\t{linha_str}")

    def seta_informacao(self, i, V):
        if 0 <= i < self.num_vertices:
            self.vertices[i].informacao = str(V)
        else:
            print("Erro: Vértice inexistente.")

    def adjacentes(self, i, adj):
        if 0 <= i < self.num_vertices:
            adj.clear()
            for aresta in self.vertices[i].adjacencias:
                adj.append(aresta.destino)
            return len(adj)
        return 0