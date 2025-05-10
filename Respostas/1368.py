import heapq

class Solution:
    def minCost(self, grid):
        m, n = len(grid), len(grid[0])
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Direita, Esquerda, Baixo, Cima
        heap = [(0, 0, 0)]  # (custo, linha, coluna)
        visited = [[False] * n for _ in range(m)]

        while heap:
            cost, i, j = heapq.heappop(heap)
            if visited[i][j]:
                continue
            visited[i][j] = True
            if i == m - 1 and j == n - 1:
                return cost
            for d, (dx, dy) in enumerate(dirs):
                ni, nj = i + dx, j + dy
                if 0 <= ni < m and 0 <= nj < n and not visited[ni][nj]:
                    if grid[i][j] == d + 1:
                        heapq.heappush(heap, (cost, ni, nj))
                    else:
                        heapq.heappush(heap, (cost + 1, ni, nj))
