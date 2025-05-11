class UnionFind:
    def __init__(self, n):
        self.pai = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.pai[x] != x:
            self.pai[x] = self.find(self.pai[x])
        return self.pai[x]

    def union(self, x, y):
        raiz_x = self.find(x)
        raiz_y = self.find(y)
        if raiz_x == raiz_y:
            return False
        if self.rank[raiz_x] < self.rank[raiz_y]:
            self.pai[raiz_x] = raiz_y
        else:
            self.pai[raiz_y] = raiz_x
            if self.rank[raiz_x] == self.rank[raiz_y]:
                self.rank[raiz_x] += 1
        return True

class Solution(object):
    def findCriticalAndPseudoCriticalEdges(self, n, arestas):
        arestas_indexadas = [aresta + [i] for i, aresta in enumerate(arestas)]
        arestas_indexadas.sort(key=lambda x: x[2])

        def kruskal(ignorar_indice=-1, forcar_aresta=None):
            uniao = UnionFind(n)
            custo = 0
            contador = 0

            if forcar_aresta:
                a, b, peso, _ = forcar_aresta
                if uniao.union(a, b):
                    custo += peso
                    contador += 1

            for i, (a, b, peso, indice) in enumerate(arestas_indexadas):
                if i == ignorar_indice:
                    continue
                if uniao.union(a, b):
                    custo += peso
                    contador += 1
                if contador == n - 1:
                    break

            return custo if contador == n - 1 else float('inf')

        custo_mst = kruskal()
        criticas = []
        pseudo_criticas = []

        for i, aresta in enumerate(arestas_indexadas):
            if kruskal(ignorar_indice=i) > custo_mst:
                criticas.append(aresta[3])
            elif kruskal(forcar_aresta=aresta) == custo_mst:
                pseudo_criticas.append(aresta[3])

        return [criticas, pseudo_criticas]
