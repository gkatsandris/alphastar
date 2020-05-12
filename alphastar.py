# -*- coding: utf-8 -*-
import graph

if __name__ == "__main__":
    V = 5
    g = graph.Graph(V)
    g.add_edge(0, 1, 1)
    g.add_edge(0, 4, 1)
    g.add_edge(1, 2, 1)
    g.add_edge(1, 3, 1)
    g.add_edge(1, 4, 1)
    g.add_edge(2, 3, 1)
    g.add_edge(3, 4, 1)
  
    g.print_graph() 