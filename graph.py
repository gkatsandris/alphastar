# -*- coding: utf-8 -*-

class AdjacencyListCell:
    def __init__(self,adjacent_vertex_id,edge_cost,former_first_adjacent_cell):
        self.vertex_id = adjacent_vertex_id
        self.cost = edge_cost
        self.next = former_first_adjacent_cell

class Graph:
    def __init__(self,vertex_number):
        self.vertex_number = vertex_number
        self.graph = [None] * self.vertex_number
        
    def add_edge(self,src,dest,cost):        
        #prepend dest's index to src's adjacency list
        self.graph[src] = AdjacencyListCell(dest,cost,self.graph[src])
        
        #prepend src's index to dest's adjacency list (undirected graph is assumed)
        self.graph[dest] = AdjacencyListCell(src,cost,self.graph[dest])
        
    def print_graph(self): 
        print("<vertex>: <neighbour>(<edge cost>), ...")
        for i in range(self.vertex_number): 
            print("v{}: ".format(i), end="") 
            temp = self.graph[i] 
            while temp: 
                print("v{}({})".format(temp.vertex_id,temp.cost), end="") 
                temp = temp.next
                if (temp): print(",",end="")
            print(" \n",end="")
            
if __name__ == "__main__":
    V = 5
    g = Graph(V) 
    g.add_edge(0, 1, 7) 
    g.add_edge(0, 4, 7) 
    g.add_edge(1, 2, 7) 
    g.add_edge(1, 3, 7) 
    g.add_edge(1, 4, 7) 
    g.add_edge(2, 3, 7) 
    g.add_edge(3, 4, 7) 
  
    g.print_graph()