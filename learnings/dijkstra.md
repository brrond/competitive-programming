# Dijkstra Algorithm

Type: greedy
Complexity: depends on implementation; O((V + E) log V)
Problem: shortest path from `src` to all other nodes

## Main Idea

The smallest path from the source to all other nodes is the smallest path from each node to the next one until destination.

## Implementation

If the graph is given as the matrix of nodes (N * N), initial state of the matrix and solution can be described by this matrix.

To implement the method, priority queue should be used. Each element of the queue is the next nearest node (in python it can be presented as tuple with node index and path cost).

Create initial state:
```python
pq = []  # priority queue (min-heap)

# add "initial" state
for j, cost in enumerate(d[s]):

    # skip self
    if cost == 0:
        continue

    heapq.heappush(pq, (cost, j))
```

```python
while len(pq) != 0:

    # get nearest vertex
    cost_to_i, i = heapq.heappop(pq)

    # skip it, if there are better theories in the queue
    if cost_to_i > d[s][i]:
        continue

    # iterate over all connected vertices 
    # that are connected to current
    for j, cost_from_i_to_j in enumerate(d[i]):

        # skip self
        if cost_from_i_to_j == 0:
            continue

        # calculate alternative path from source
        # via this vertex
        alternative = cost_to_i + cost_from_i_to_j

        if alternative < d[s][j]:
            d[s][j] = alternative
            heapq.heappush(pq, (alternative, j))
```

## Links

- https://www.geeksforgeeks.org/dsa/introduction-to-dijkstras-shortest-path-algorithm/
- https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm#Using_a_priority_queue

