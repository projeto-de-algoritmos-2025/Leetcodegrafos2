import heapq
from collections import defaultdict

class Solution:
    def networkDelayTime(self, tempos, n, k):
        grafo = defaultdict(list)
        for origem, destino, peso in tempos:
            grafo[origem].append((destino, peso))

        fila = [(0, k)]  
        tempos_minimos = {}  

        while fila:
            tempo_atual, no_atual = heapq.heappop(fila)
            if no_atual in tempos_minimos:
                continue
            tempos_minimos[no_atual] = tempo_atual
            for vizinho, custo in grafo[no_atual]:
                if vizinho not in tempos_minimos:
                    heapq.heappush(fila, (tempo_atual + custo, vizinho))

        if len(tempos_minimos) != n:
            return -1
        return max(tempos_minimos.values())
