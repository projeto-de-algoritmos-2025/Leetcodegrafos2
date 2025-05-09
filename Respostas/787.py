import heapq
from collections import defaultdict

class Solution:
    def findCheapestPrice(self, n, flights, src, dst, k):
        graph = defaultdict(list)
        for u, v, price in flights:
            graph[u].append((v, price))
        
        heap = [(0, src, 0)]  # (custo acumulado, cidade atual, paradas)
        
        # visited[(cidade, paradas)] = menor custo conhecido
        visited = dict()

        while heap:
            cost, node, stops = heapq.heappop(heap)
            
            # Se chegamos ao destino, retornamos o custo
            if node == dst:
                return cost
            
            # Se já visitamos essa cidade com menos paradas e custo menor, ignoramos
            if (node, stops) in visited and visited[(node, stops)] <= cost:
                continue
            visited[(node, stops)] = cost

            # Explorar os vizinhos se ainda não excedemos o número de paradas
            if stops <= k:
                for neighbor, price in graph[node]:
                    heapq.heappush(heap, (cost + price, neighbor, stops + 1))
        
        return -1
