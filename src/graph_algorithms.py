import heapq

class GraphAlgorithms:
    @staticmethod
    def kruskal(num_nodes, edges):
        """Kruskal's algorithm using Union-Find for MST."""
        parent = list(range(num_nodes))
        rank = [0] * num_nodes

        def find(i):
            if parent[i] == i:
                return i
            parent[i] = find(parent[i])
            return parent[i]

        def union(i, j):
            root_i = find(i)
            root_j = find(j)
            if root_i != root_j:
                if rank[root_i] < rank[root_j]:
                    parent[root_i] = root_j
                elif rank[root_i] > rank[root_j]:
                    parent[root_j] = root_i
                else:
                    parent[root_j] = root_i
                    rank[root_i] += 1
                return True
            return False

        # Sort edges by weight
        sorted_edges = sorted(edges, key=lambda item: item[2])
        mst = []
        total_cost = 0
        for u, v, weight in sorted_edges:
            if union(u, v):
                mst.append((u, v, weight))
                total_cost += weight
        return mst, total_cost

    @staticmethod
    def prim(num_nodes, adj_list):
        """Prim's algorithm for MST using priority queue."""
        visited = [False] * num_nodes
        min_heap = [(0, 0, -1)]  # (weight, u, parent)
        mst = []
        total_cost = 0

        while min_heap:
            weight, u, parent = heapq.heappop(min_heap)
            if visited[u]:
                continue
            visited[u] = True
            if parent != -1:
                mst.append((parent, u, weight))
                total_cost += weight
            for v, w in adj_list[u]:
                if not visited[v]:
                    heapq.heappush(min_heap, (w, v, u))
        return mst, total_cost

    @staticmethod
    def floyd_warshall(num_nodes, dist_matrix):
        """All-pairs shortest path cost analysis."""
        dist = [row[:] for row in dist_matrix]
        for k in range(num_nodes):
            for i in range(num_nodes):
                for j in range(num_nodes):
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
        return dist
