from graph_algorithms import GraphAlgorithms
from optimization import OptimizationAlgorithms

if __name__ == "__main__":
    print("=== Running Network Optimization Framework ===")
    
    # 1. MST Demonstration
    num_nodes = 4
    edges = [(0, 1, 10), (0, 2, 6), (0, 3, 5), (1, 3, 15), (2, 3, 4)]
    adj_list = {0: [(1,10), (2,6), (3,5)], 1: [(0,10), (3,15)], 2: [(0,6), (3,4)], 3: [(0,5), (1,15), (2,4)]}
    
    mst_k, cost_k = GraphAlgorithms.kruskal(num_nodes, edges)
    mst_p, cost_p = GraphAlgorithms.prim(num_nodes, adj_list)
    print(f"Kruskal MST Cost: {cost_k}")
    print(f"Prim MST Cost: {cost_p}")

    # 2. Floyd-Warshall All-Pairs Cost Analysis
    inf = float('inf')
    cost_matrix = [
        [0, 3, inf, 7],
        [8, 0, 2, inf],
        [5, inf, 0, 1],
        [2, inf, inf, 0]
    ]
    all_pairs = GraphAlgorithms.floyd_warshall(4, cost_matrix)
    print("Floyd-Warshall All-Pairs Shortest Paths Computed.")

    # 5. Upgrade Budgeting
    items = [(60, 10, "Upgrade A"), (100, 20, "Upgrade B"), (120, 30, "Upgrade C")]
    val_frac, details = OptimizationAlgorithms.fractional_knapsack(items, 50)
    print(f"Fractional Knapsack Max Value: {val_frac}")
    
    val_01 = OptimizationAlgorithms.knapsack_01([60, 100, 120], [10, 20, 30], 50)
    print(f"0/1 Knapsack Max Value: {val_01}")

    # 6. Maintenance Tour (TSP)
    tsp_matrix = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]
    min_tsp_cost, path = OptimizationAlgorithms.tsp_backend = OptimizationAlgorithms.tsp_backtracking(4, tsp_matrix)
    print(f"TSP Minimum Maintenance Tour Cost: {min_tsp_cost} with Path: {path}")
