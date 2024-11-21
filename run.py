# Search methods

from search import *
import time

ab = GPSProblem('A', 'B'
                       , romania)

og = GPSProblem('O', 'G'
                       , romania)

ch = GPSProblem('C', 'H'
                       , romania)

lu = GPSProblem('L', 'U'
                       , romania)

# Breadth-First Search
print("\n--------------")
print("Breadth-First Search")
start_time = time.time()
bfs_result = breadth_first_graph_search(ab)
end_time = time.time()
print("Result:", bfs_result.path())
print(f"Execution Time: {end_time - start_time:.6f} seconds")
print("--------------\n")

# Depth-First Search
print("--------------")
print("Depth-First Search")
start_time = time.time()
dfs_result = depth_first_graph_search(ab)
end_time = time.time()
print("Result:", dfs_result.path())
print(f"Execution Time: {end_time - start_time:.6f} seconds")
print("--------------\n")

# Branch and baund
print("--------------")
print("Branch and baund")
start_time = time.time()
ram_result = branch_and_baund(ab)
end_time = time.time()
print("Result:", ram_result.path())
print(f"Execution Time: {end_time - start_time:.6f} seconds")
print("--------------\n")

# Branch and baund underestimation
print("--------------")
print("Branch and baund underestimation")
start_time = time.time()
ram_result = branch_and_baund_underestimation(ab)
end_time = time.time()
print("Result:", ram_result.path())
print(f"Execution Time: {end_time - start_time:.6f} seconds")
print("--------------\n")



