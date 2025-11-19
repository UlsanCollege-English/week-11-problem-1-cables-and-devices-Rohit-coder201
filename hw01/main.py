"""
HW01 — Cables and Devices (package copy)

Provides:
- build_graph(edges, directed=False)
- degree_dict(graph)

This file mirrors the top-level `main.py` implementation so tests can import
from `hw01.main` as expected.
Do NOT add type hints. Use only the standard library.
"""

def build_graph(edges, directed=False):
    # make empty graph
    graph = {}

    # go through each edge
    for u, v in edges:
        # always add u -> v
        if u not in graph:
            graph[u] = []
        graph[u].append(v)

        # if undirected also add v -> u
        if not directed:
            if v not in graph:
                graph[v] = []
            graph[v].append(u)

        # if directed but v not added yet, create empty list
        elif v not in graph:
            graph[v] = []

    return graph


def degree_dict(graph):
    # degree is just number of neighbors
    deg = {}
    for node in graph:
        deg[node] = len(graph[node])
    return deg


if __name__ == "__main__":
    # Optional manual check
    sample = [('PC1','SW1'), ('SW1','PR1'), ('PR1','PC2')]
    print("Sample edges:", sample)
    # Fill in calls below after you implement functions
    g = build_graph(sample, directed=False)
    print("Graph:", g)
    print("Degrees:", degree_dict(g))
