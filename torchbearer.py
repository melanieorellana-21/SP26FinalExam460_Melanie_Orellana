"""
CS 460 – Algorithms: Final Programming Assignment
The Torchbearer

Student Name: ____Melanie Orellana_______________________
Student ID:   _____130055910______________________

INSTRUCTIONS
------------
- Implement every function marked TODO.
- Do not change any function signature.
- Do not remove or rename required functions.
- You may add helper functions.
- Variable names in your code must match what you define in README Part 5a.
- The pruning safety comment inside _explore() is graded. Do not skip it.

Submit this file as: torchbearer.py
"""

import heapq



# =============================================================================
# PART 1
# =============================================================================

def explain_problem():
    """
    Returns
    -------
    str
        Your Part 1 README answers, written as a string.
        Must match what you wrote in README Part 1.

    TODO
    """
    return (
        "While a single shortest-path run gives us the paths with the minimum costs, in this problem the torchbearer is also attempting to fingure out in which order to visit the relics as well because different orders may give us a different reult."
        "The order in which teh torchbearer chooses to visit the relics."
        "This requires search over orders because different orders of relics can result in different total cost.")


# =============================================================================
# PART 2
# =============================================================================

def select_sources(spawn, relics, exit_node):
    """
    Parameters
    ----------
    spawn : node
    relics : list[node]
    exit_node : node

    Returns
    -------
    list[node]
        No duplicates. Order does not matter.

    TODO
    """
    sources = set()

    sources.add(spawn)

    for relic in relics:
        sources.add(relic)


    return list(sources)


def run_dijkstra(graph, source):
    """
    Parameters
    ----------
    graph : dict[node, list[tuple[node, int]]]
        graph[u] = [(v, cost), ...]. All costs are nonnegative integers.
    source : node

    Returns
    -------
    dict[node, float]
        Minimum cost from source to every node in graph.
        Unreachable nodes map to float('inf').

    TODO
    """

    dist = dict()

    for node in graph:
        dist[node] = float('inf')

    dist[source] = 0
    priority_queue = [(0, source)]

    while priority_queue:
        current_dist, current_node = heapq.heappop(priority_queue)

        if current_dist > dist[current_node]:
            continue

        for neighbor, cost in graph[current_node]:
            distance = current_dist + cost

            if distance < dist[neighbor]:
                dist[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return dist


def precompute_distances(graph, spawn, relics, exit_node):
    """
    Parameters
    ----------
    graph : dict[node, list[tuple[node, int]]]
    spawn : node
    relics : list[node]
    exit_node : node

    Returns
    -------
    dict[node, dict[node, float]]
        Nested structure supporting dist_table[u][v] lookups
        for every source u your design requires.

    TODO
    """

    dist_table = dict()

    sources = select_sources(spawn, relics, exit_node)

    for source in sources:
        dist_table[source] = run_dijkstra(graph, source)
    
    return dist_table


# =============================================================================
# PART 3
# =============================================================================

def dijkstra_invariant_check():
    """
    Returns
    -------
    str
        Your Part 3 README answers, written as a string.
        Must match what you wrote in README Part 3.

    TODO
    """
    return (
        "Part A:"
        "These nodes have a shortest-path finalized with minimal cost, therefore their paths are finalized."
        "These nodes have a version of a shortest-path found but there are still other possibilities that may give us a smaller cost, therefore they are not finalized."
        "Part B:"
        "At the start, we are at Node S, it does not take any fuel to be at Node S hence, the total cost is 0 while every other node does not have a definitive cost since we have not started traversing."
        "Finalizing the mid-dist node is always correct because any other path would require us to add any nonnegative edge weights, furthermore not making this the shortest path."
        "The invariant guarentees that every node has a shortest-path which has been found once the algoirthm ends."
        "Part C:"
        "Having the correct shortest-path is needed because the route planner need accurate calcuations to decide the optimal order of relics which will ultimately lead to total minimum cost."
    )


# =============================================================================
# PART 4
# =============================================================================

def explain_search():
    """
    Returns
    -------
    str
        Your Part 4 README answers, written as a string.
        Must match what you wrote in README Part 4.

    TODO
    """
    return "T- **The failure mode:** _Greedy fails, while greedy calculates the shortest-path from every relic to the start node, the order that we choose to visit the relics later can result in a cheaper cost._"
"- **Counter-example setup:** _Suppse the torchbearer starts at node S and must visit relics B, C, and D before reaching the exit-node T. S -> B costs 2, S -> C costs 5, and S-> D costs 2._"
"- **What greedy picks:** _Greedy will choose the relic with the currect cheapest path._"
"- **What optimal picks:** _The optimal solution might pick D because it can produce a overall lower cost._"
"- **Why greedy loses:** _Greedy only considers local decsions while the optimal solution can later produce cheapper routes by making decsions for routes later considering every possibility and ultimately choosing the cheapest path._"


# =============================================================================
# PARTS 5 + 6
# =============================================================================

def find_optimal_route(dist_table, spawn, relics, exit_node):
    """
    Parameters
    ----------
    dist_table : dict[node, dict[node, float]]
        Output of precompute_distances.
    spawn : node
    relics : list[node]
        Every node in this list must be visited at least once.
    exit_node : node
        The route must end here.

    Returns
    -------
    tuple[float, list[node]]
        (minimum_fuel_cost, ordered_relic_list)
        Returns (float('inf'), []) if no valid route exists.

    TODO
    """
    best_order = [float('inf'), []]


    relics_remaining = set(relics)

    visited_order = []

    _explore(dist_table, spawn, relics_remaining, visited_order, 0, exit_node, best_order)

    if best_order[0] == float('inf'):
        return (float('inf'), [])
    
    return  (best_order[0], best_order[1])


def _explore(dist_table, current_loc, relics_remaining, relics_visited_order,
             cost_so_far, exit_node, best):
    """
    Recursive helper for find_optimal_route.

    Parameters
    ----------
    dist_table : dict[node, dict[node, float]]
    current_loc : node
    relics_remaining : collection
        Your chosen data structure from README Part 5b.
    relics_visited_order : list[node]
    cost_so_far : float
    exit_node : node
    best : list
        Mutable container for the best solution found so far.

    Returns
    -------
    None
        Updates best in place.

    TODO
    Implement: base case, pruning, recursive case, backtracking.

    REQUIRED: Add a 1-2 sentence comment near your pruning condition
    explaining why it is safe (cannot skip the optimal solution).
    This comment is graded.
    """

    if not relics_remaining:
        tot_cost = cost_so_far + dist_table[current_loc][exit_node]

        if exit_node not in dist_table[current_loc] or tot_cost < best[0]:
                best[0] = tot_cost
                best[1] = relics_visited_order.copy()

        tot_cost = cost_so_far + dist_table[current_loc][exit_node]

        if tot_cost < best[0]:
            best[0] = tot_cost
            best[1] = relics_visited_order.copy()
        
        return
    
    for relic in relics_remaining:
        new_cost = cost_so_far + dist_table[current_loc][relic]

        #Pruning: if the cost to the next relic is greater than the cost found previously, we can safely skip exploring this path since a shorter path cannot be found. If we were to explore this path then we would be adding more to the paths cost thus it would not be optimal.
        if relic not in dist_table[current_loc] or new_cost >= best[0]:
           continue

        relics_remaining.remove(relic)
        relics_visited_order.append(relic)

        _explore(dist_table, relic, relics_remaining, relics_visited_order,
                 new_cost, exit_node, best)
        
        
        relics_visited_order.pop()
        relics_remaining.add(relic)

        


# =============================================================================
# PIPELINE
# =============================================================================

def solve(graph, spawn, relics, exit_node):
    """
    Parameters
    ----------
    graph : dict[node, list[tuple[node, int]]]
    spawn : node
    relics : list[node]
    exit_node : node

    Returns
    -------
    tuple[float, list[node]]
        (minimum_fuel_cost, ordered_relic_list)
        Returns (float('inf'), []) if no valid route exists.

    TODO
    """
    pass


# =============================================================================
# PROVIDED TESTS (do not modify)
# Graders will run additional tests beyond these.
# =============================================================================

def _run_tests():
    print("Running provided tests...")

    # Test 1: Spec illustration. Optimal cost = 4.
    graph_1 = {
        'S': [('B', 1), ('C', 2), ('D', 2)],
        'B': [('D', 1), ('T', 1)],
        'C': [('B', 1), ('T', 1)],
        'D': [('B', 1), ('C', 1)],
        'T': []
    }
    cost, order = solve(graph_1, 'S', ['B', 'C', 'D'], 'T')
    assert cost == 4, f"Test 1 FAILED: expected 4, got {cost}"
    print(f"  Test 1 passed  cost={cost}  order={order}")

    # Test 2: Single relic. Optimal cost = 5.
    graph_2 = {
        'S': [('R', 3)],
        'R': [('T', 2)],
        'T': []
    }
    cost, order = solve(graph_2, 'S', ['R'], 'T')
    assert cost == 5, f"Test 2 FAILED: expected 5, got {cost}"
    print(f"  Test 2 passed  cost={cost}  order={order}")

    # Test 3: No valid path to exit. Must return (inf, []).
    graph_3 = {
        'S': [('R', 1)],
        'R': [],
        'T': []
    }
    cost, order = solve(graph_3, 'S', ['R'], 'T')
    assert cost == float('inf'), f"Test 3 FAILED: expected inf, got {cost}"
    print(f"  Test 3 passed  cost={cost}")

    # Test 4: Relics reachable only through intermediate rooms.
    # Optimal cost = 6.
    graph_4 = {
        'S': [('X', 1)],
        'X': [('R1', 2), ('R2', 5)],
        'R1': [('Y', 1)],
        'Y': [('R2', 1)],
        'R2': [('T', 1)],
        'T': []
    }
    cost, order = solve(graph_4, 'S', ['R1', 'R2'], 'T')
    assert cost == 6, f"Test 4 FAILED: expected 6, got {cost}"
    print(f"  Test 4 passed  cost={cost}  order={order}")

    # Test 5: Explanation functions must return non-placeholder strings.
    for fn in [explain_problem, dijkstra_invariant_check, explain_search]:
        result = fn()
        assert isinstance(result, str) and result != "TODO" and len(result) > 20, \
            f"Test 5 FAILED: {fn.__name__} returned placeholder or empty string"
    print("  Test 5 passed  explanation functions are non-empty")

    print("\nAll provided tests passed.")


if __name__ == "__main__":
    #_run_tests()
    if __name__ == "__main__":
     dist_table = {
        "S": {"B": 1, "C": 2, "D": 2, "T": float("inf")},
        "B": {"B": 0, "C": 100, "D": 1, "T": 1},
        "C": {"B": 1, "C": 0, "D": 100, "T": 1},
        "D": {"B": 1, "C": 1, "D": 0, "T": 100},
    }

    spawn = "S"
    relics = ["B", "C", "D"]
    exit_node = "T"

    result = find_optimal_route(dist_table, spawn, relics, exit_node)

    print("Result:", result)
    print("Expected cost: 4")
    print("Expected order: ['B', 'D', 'C']")
