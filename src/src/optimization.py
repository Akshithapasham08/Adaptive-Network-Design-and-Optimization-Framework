class OptimizationAlgorithms:
    @staticmethod
    def fractional_knapsack(items, capacity):
        """Greedy approach for divisible network-upgrade cases."""
        # items = list of tuples: (value, weight, name)
        sorted_items = sorted(items, key=lambda x: x[0]/x[1], reverse=True)
        total_value = 0.0
        details = []

        for value, weight, name in sorted_items:
            if capacity >= weight:
                capacity -= weight
                total_value += value
                details.append((name, 1.0))
            else:
                fraction = capacity / weight
                total_value += value * fraction
                details.append((name, fraction))
                break
        return total_value, details

    @staticmethod
    def knapsack_01(values, weights, capacity):
        """Dynamic programming approach for indivisible network upgrades."""
        n = len(values)
        dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

        for i in range(1, n + 1):
            for w in range(1, capacity + 1):
                if weights[i-1] <= w:
                    dp[i][w] = max(values[i-1] + dp[i-1][w - weights[i-1]], dp[i-1][w])
                else:
                    dp[i][w] = dp[i-1][w]
        return dp[n][capacity]

    @staticmethod
    def tsp_backtracking(num_nodes, cost_matrix):
        """Exact combinatorial search for maintenance tour (TSP)."""
        visited = [False] * num_nodes
        min_cost = float('inf')
        best_path = []

        def dfs(curr_node, count, current_cost, path):
            nonlocal min_cost, best_path
            if count == num_nodes and cost_matrix[curr_node][0] > 0:
                total = current_cost + cost_matrix[curr_node][0]
                if total < min_cost:
                    min_cost = total
                    best_path = path + [0]
                return

            for i in range(num_nodes):
                if not visited[i] and cost_matrix[curr_node][i] > 0:
                    visited[i] = True
                    dfs(i, count + 1, current_cost + cost_matrix[curr_node][i], path + [i])
                    visited[i] = False

        visited[0] = True
        dfs(0, 1, 0, [0])
        return min_cost, best_path
