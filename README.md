# The Torchbearer

**Student Name:** _Melanie Orellana__________________________
**Student ID:** __130055910_________________________
**Course:** CS 460 – Algorithms | Spring 2026

> This README is your project documentation. Write it the way a developer would document
> their design decisions , bullet points, brief justifications, and concrete examples where
> required. You are not writing an essay. You are explaining what you built and why you built
> it that way. Delete all blockquotes like this one before submitting.

---

## Part 1: Problem Analysis

> Document why this problem is not just a shortest-path problem. Three bullet points, one
> per question. Each bullet should be 1-2 sentences max.

- **Why a single shortest-path run from S is not enough:**
  _ While a single shortest-path run gives us the paths with the minimum costs, in this problem the torchbearer is also attempting to fingure out in which order to visit the relics as well because different orders may give us a different reult._

- **What decision remains after all inter-location costs are known:**
  _The order in which teh torchbearer chooses to visit the relics_

- **Why this requires a search over orders (one sentence):**
  _This requires search over orders because different orders of relics can result in different total cost._

---

## Part 2: Precomputation Design

### Part 2a: Source Selection

> List the source node types as a bullet list. For each, one-line reason.

| Source Node Type | Why it is a source |
|---|---|
| _Start Node S_ | _The algorithm needs a start node in order to compute the shortest-path from a starting point._ |
| _Relic nodes in M_ | _One of the requirments have us visit every relic in M and we must see which paths produce the shortest-path with minimal cost._ |

### Part 2b: Distance Storage

> Fill in the table. No prose required.

| Property | Your answer |
|---|---|
| Data structure name | hash map |
| What the keys represent | (u,v) important nodes to take into account |
| What the values represent | the minimum cost from u to v |
| Lookup time complexity | O(1) |
| Why O(1) lookup is possible | hash tables allow for direct access to keys |

### Part 2c: Precomputation Complexity

> State the total complexity and show the arithmetic. Two to three lines max.

- **Number of Dijkstra runs:** _k+1_
- **Cost per run:** _O(m log n)_
- **Total complexity:** _O((k+1)m log n)_
- **Justification (one line):** _Dijkstra will run once from node S to Node T ensuring every relic is visited using a priority queue._

---

## Part 3: Algorithm Correctness

> Document your understanding of why Dijkstra produces correct distances.
> Bullet points and short sentences throughout. No paragraphs.

### Part 3a: What the Invariant Means

> Two bullets: one for finalized nodes, one for non-finalized nodes.
> Do not copy the invariant text from the spec.

- **For nodes already finalized (in S):**
  _These nodes have a shortest-path finalized with minimal cost, therefore their paths are finalized._

- **For nodes not yet finalized (not in S):**
  _These nodes have a version of a shortest-path found but there are still other possibilities that may give us a smaller cost, therefore they are not finalized._

### Part 3b: Why Each Phase Holds

> One to two bullets per phase. Maintenance must mention nonnegative edge weights.

- **Initialization : why the invariant holds before iteration 1:**
  _At the start, we are at Node S, it does not take any fuel to be at Node S hence, the total cost is 0 while every other node does not have a definitive cost since we have not started traversing._

- **Maintenance : why finalizing the min-dist node is always correct:**
  _Finalizing the mid-dist node is always correct because any other path would require us to add any nonnegative edge weights, furthermore not making this the shortest path. _

- **Termination : what the invariant guarantees when the algorithm ends:**
  _The invariant guarentees that every node has a shortest-path which has been found once the algoirthm ends._

### Part 3c: Why This Matters for the Route Planner

> One sentence connecting correct distances to correct routing decisions.

_Having the correct shortest-path is needed because the route planner need accurate calcuations to decide the optimal order of relics which will ultimately lead to total minimum cost._

---

## Part 4: Search Design

### Why Greedy Fails

> State the failure mode. Then give a concrete counter-example using specific node names
> or costs (you may use the illustration example from the spec). Three to five bullets.

- **The failure mode:** _Your answer here._
- **Counter-example setup:** _Your answer here._
- **What greedy picks:** _Your answer here._
- **What optimal picks:** _Your answer here._
- **Why greedy loses:** _Your answer here._

### What the Algorithm Must Explore

> One bullet. Must use the word "order."

- _Your answer here._

---

## Part 5: State and Search Space

### Part 5a: State Representation

> Document the three components of your search state as a table.
> Variable names here must match exactly what you use in torchbearer.py.

| Component | Variable name in code | Data type | Description |
|---|---|---|---|
| Current location | | | |
| Relics already collected | | | |
| Fuel cost so far | | | |

### Part 5b: Data Structure for Visited Relics

> Fill in the table.

| Property | Your answer |
|---|---|
| Data structure chosen | |
| Operation: check if relic already collected | Time complexity: |
| Operation: mark a relic as collected | Time complexity: |
| Operation: unmark a relic (backtrack) | Time complexity: |
| Why this structure fits | |

### Part 5c: Worst-Case Search Space

> Two bullets.

- **Worst-case number of orders considered:** _Your answer (in terms of k)._
- **Why:** _One-line justification._

---

## Part 6: Pruning

### Part 6a: Best-So-Far Tracking

> Three bullets.

- **What is tracked:** _Your answer here._
- **When it is used:** _Your answer here._
- **What it allows the algorithm to skip:** _Your answer here._

### Part 6b: Lower Bound Estimation

> Three bullets.

- **What information is available at the current state:** _Your answer here._
- **What the lower bound accounts for:** _Your answer here._
- **Why it never overestimates:** _Your answer here._

### Part 6c: Pruning Correctness

> One to two bullets. Explain why pruning is safe.

- _Your answer here._

---

## References

> Bullet list. If none beyond lecture notes, write that.

- _Your references here._
