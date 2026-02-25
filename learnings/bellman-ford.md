# Bellman-Ford Algorithm

Type: DP
Complexity: O(nm)
Problem: smallest path from `src` to `dst` in graph.

In comparison to Dijkstra, works in graphs with negative cycles (and negative edges).

## Main Idea

Each edge of the graph is being iterated and "relaxed". Basically:
```python
d[j] = min(d[j], d[i] + cost)
```

The process of edge relaxation must be done V - 1 time (as each vertex can be connected with each vertex and in this case the total number of required operations is V - 1, because total number of edges is $E = V * (V - 1) / 2$).

## Implementation

Python-Pseudocode:

```python
d[n] <- +inf
d[0] = 0

for _ in range(V - 1):

    for edge in edges:

        d[edge.to] = min(
            d[edge.to],
            d[edge.from] + edge.cost
        )

return d[-1]
```

## Links

- https://www.geeksforgeeks.org/dsa/bellman-ford-algorithm-dp-23/


