# Development Log – The Torchbearer

**Student Name:** _Melanie Orellana__________________________
**Student ID:** __130055910_________________________

> Instructions: Write at least four dated entries. Required entry types are marked below.
> Two to five sentences per entry is sufficient. Write entries as you go, not all in one
> sitting. Graders check that entries reflect genuine work across multiple sessions.
> Delete all blockquotes before submitting.

---

## Entry 1 – [Date]: Initial Plan

> Required. Write this before writing any code. Describe your plan: what you will
> implement first, what parts you expect to be difficult, and how you plan to test.

_For this programming assignment, I will be splitting up the work into four different parts. For day one, I will complete my first DEVLOG entry, the first three parts of the README, and work on the three functions in torchbearer.py: explain_problem(), select_sources(), and dijkstra_invariant_check(). On day two, I plan to implement run_dijkstra() and precompute_distances(); these functions will help me find the shortest path from the starting node to every other node, hence ultimately finding the shortest path with minimum cost. After completing both implementations, I will test the functions on smaller graphs to ensure my program is running as expected. Then I will update my README and commit to the DEVLOG. For day three, I plan to implement find_optimal_route(), _explore(), and work through parts 4, 5, and 6 of my README. These functions will decide which relics to visit first after computing the shortest paths through Dijkstra. I will also be pruning with best-so-far. I will also add to my DEVLOG for any bugs found along the way and or design changes. On the final day, I will be testing my code and ensuring that everything is as needed to get ready for submission. Lastly, I will make my last DEVLOG commit. When testing, I will use smaller graphs for the initial testing, then move on to slightly more complicated tests. I expect the most difficult part of this assignment to be the testing portion and debugging/any design changes needed._

---

## Entry 2 – [Date]: [Short description]

> Required. At least one entry must describe a bug, wrong assumption, or design change
> you encountered. Describe what went wrong and how you resolved it.

_Today, I implemented Dijkstra and distance precomputation. I ran into a small bug in run_dijkstra as I forgot to push the new distances into the priority queue after updating them. Also ran into small bugs with the initialization of the dictionary in run_dijkstra, and while I didn't think I needed to initialize sources in precompute_distances with the exit_node as well, I found it was required to do so. I also made a slight change to my README Part 2c since I realized that the analysis part of my response was incorrect._

---

## Entry 3 – [Date]: [Short description]

_Today I implemented find_optimal_route() and _explore(). I ran into problems with the final route not updating correctly. I attempted to store min_cost and best_order separately, but found it was better to use a mutable container, which ultimately allowed for the final route to be stored correctly. I also ran into a bug when I was storing distances in the wrong direction, so instead of dist_table[current_loc][exit_node], I was doing the opposite. Today, I figured out how the backtracking would work in terms of tracking the current relic, remaining relics, visited order, and total cost. I also completed the explain_search() in torchbearer.py._

---

## Entry 4 – [Date]: Post-Implementation Reflection

> Required. Written after your implementation is complete. Describe what you would
> change or improve given more time.

_If I were to have more time, I would improve the pruning strategy to accommodate larger graphs, and I would also account for additional edge cases as well. Overall, some portions of this assignment did take me longer than I would have expected, but given more time, I would implement a better strategy to improve efficiency._

---

## Final Entry – [Date]: Time Estimate

> Required. Estimate minutes spent per part. Honesty is expected; accuracy is not graded.

| Part | Estimated Hours |
|---|---|
| Part 1: Problem Analysis | 1 |
| Part 2: Precomputation Design | 2 |
| Part 3: Algorithm Correctness | 2 |
| Part 4: Search Design | 2 |
| Part 5: State and Search Space | 2 |
| Part 6: Pruning | 2 |
| Part 7: Implementation | 5 |
| README and DEVLOG writing | 2 |
| **Total** | 18 |
