# Assignment 2
Breadth-first search

This repo contains a file, graph.py in search that performs breadth-first search. BFS is an algorithm that searches a graph and finds a traversal that is the shortest path through the graph. It utilizes a "queue," for which after a node is visited, its neighbors are added to the queue, while keeping track nodes that have already been explored.

In the case that the graph is empty, the start node provided is not in the graph, or an end node is provided that is not in the graph, it will raise a ValueError. If there is no route between the nodes and both are in the graph, it will return None. This function will provide both the shortest path between a start and end node when an end node is provided, or the full traversal of the graph with BFS when just a start node is provided.

# Ensure that GitHub Actions is run with pytest when pushed
"! [BuildStatus] (https://github.com/SarahAncheta/HW2-BFS/workflows/HW2-BFS/badge.svg?event=push)"