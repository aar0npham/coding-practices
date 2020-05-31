'''
This problem was asked by Jane Street.

Suppose you are given a table of currency exchange rates, represented as a 2D array.
Determine whether there is a possible arbitrage: that is, whether there is some sequence of trades you can make,
starting with some amount A of any currency, so that you can end up with some amount greater than A of that currency.

There are no transaction costs and you can trade fractional quantities.
(Using Bellman-Ford algorithm)
'''

from math import log

rates1 = [[1, 2, 4, 0.5], [0.5, 1, 100, 1], [.25, .01, 1, 1], [2, 1, 1, 1]]
rates2 = [[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]]

def arbitrage(rates):
    transformed_graph = [[-log(edge) for edge in row] for row in rates]

    source = 0
    n = len(transformed_graph)
    min_dist = [float('inf')]*n
    min_dist[source]=0

     # Relax edges |V - 1| times
    for i in range(n - 1):
        for v in range(n):
            for w in range(n):
                if min_dist[w] > min_dist[v] + transformed_graph[v][w]:
                    min_dist[w] = min_dist[v] + transformed_graph[v][w]

    # If we can still relax edges, then we have a negative cycle
    for v in range(n):
        for w in range(n):
            if min_dist[w] > min_dist[v] + transformed_graph[v][w]:
                return True

    return False

print(arbitrage(rates1))
