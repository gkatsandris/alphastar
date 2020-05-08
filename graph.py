# -*- coding: utf-8 -*-

class AdjacentVertexListCell:
    def __init__(self):
        self.adjacent_vertex_id = None
        self.next = None

class Graph:
    def __init__(self,vertex_number):
        self.vertex_number = vertex_number
        self.graph = [None] * self.vertex_number
        
    def add_edge(self,src,dest):        
        #prepend dest's index to src's adjacency list
        new_cell = AdjacentVertexListCell()
        new_cell.adjacent_vertex_id = dest
        new_cell.next = self.graph[src]
        self.graph[src] = new_cell
        
        #prepend src's index to dest's adjacency list (undirected graph is assumed)
        new_cell = AdjacentVertexListCell()
        new_cell.adjacent_vertex_id = src
        new_cell.next = self.graph[dest]
        self.graph[dest] = new_cell
        
    def print_graph(self): 
        for i in range(self.vertex_number): 
            print("Adjacency list of vertex {}\n head".format(i), end="") 
            temp = self.graph[i] 
            while temp: 
                print(" -> {}".format(temp.adjacent_vertex_id), end="") 
                temp = temp.next
            print(" \n") 
        
if __name__ == "__main__": 
    V = 5
    graph = Graph(V) 
    graph.add_edge(0, 1) 
    graph.add_edge(0, 4) 
    graph.add_edge(1, 2) 
    graph.add_edge(1, 3) 
    graph.add_edge(1, 4) 
    graph.add_edge(2, 3) 
    graph.add_edge(3, 4) 
  
    graph.print_graph() 