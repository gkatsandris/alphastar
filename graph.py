# -*- coding: utf-8 -*-

class AdjacencyListCell:
    def __init__(self,adjacent_vertex_id,former_first_adjacent_cell):
        self.vertex_id = adjacent_vertex_id
        self.next = former_first_adjacent_cell

class Graph:
    def __init__(self,vertex_number):
        self.vertex_number = vertex_number
        self.graph = [None] * self.vertex_number
        
    def add_edge(self,src,dest):        
        #prepend dest's index to src's adjacency list
        self.graph[src] = AdjacencyListCell(dest,self.graph[src])
        
        #prepend src's index to dest's adjacency list (undirected graph is assumed)
        self.graph[dest] = AdjacencyListCell(src,self.graph[dest])
        
    def print_graph(self): 
        for i in range(self.vertex_number): 
            print("Adjacency list of vertex {}\n head".format(i), end="") 
            temp = self.graph[i] 
            while temp: 
                print(" -> {}".format(temp.vertex_id), end="") 
                temp = temp.next
            print(" \n")