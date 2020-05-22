# -*- coding: utf-8 -*-

#Undirected graph with edge costs implementation. Includes graphviz format export functionality.

class AdjacencyListCell:
    def __init__(self,adjacent_vertex_id,edge_cost,former_first_adjacent_cell):
        self.id = adjacent_vertex_id
        self.cost = edge_cost
        self.next = former_first_adjacent_cell

class Graph:
    def __init__(self,vertex_number,type="directed"):
        valid_types = {"directed","undirected"}
        if type not in valid_types:
            raise ValueError("type must be one of %r." % valid_types)
        self.type = type
        
        self.vertex_number = vertex_number
        self.vertex_adjacency_lists = [None] * self.vertex_number
        
    def add_edge(self,src,dest,cost):        
        #prepend dest's index to src's adjacency list
        self.vertex_adjacency_lists[src] = AdjacencyListCell(dest,cost,self.vertex_adjacency_lists[src])
        
        if self.type == "undirected":
            #prepend src's index to dest's adjacency list (for undirected graphs)
            self.vertex_adjacency_lists[dest] = AdjacencyListCell(src,cost,self.vertex_adjacency_lists[dest])
        
    def print_graph(self): 
        print("<vertex>: <reachable vertex>(<edge cost>), ...")
        for i in range(self.vertex_number): 
            print("v{}: ".format(i), end="") 
            temp = self.vertex_adjacency_lists[i] 
            while temp: 
                print("v{}({})".format(temp.id,temp.cost), end="") 
                temp = temp.next
                if temp: print(",",end="")
            print(" \n",end="")
            
    def export_graphviz(self):
        if self.type == "directed":
            string = "digraph {\nrankdir=LR\n"
            for i in range(self.vertex_number):
                temp = self.vertex_adjacency_lists[i]
                while temp:
                    string += (
                        "v"
                        + str(i)
                        + "->v"
                        + str(temp.id)
                        + " [label="
                        + str(temp.cost)
                        + "]\n"
                    )
                    temp = temp.next
            string = string + "}"
        if self.type == "undirected":
            string = "strict graph {\nrankdir=LR\n"
            for i in range(self.vertex_number):
                temp = self.vertex_adjacency_lists[i]
                while temp:
                    string += (
                        "v"
                        + str(i)
                        + "--v"
                        + str(temp.id)
                        + " [label="
                        + str(temp.cost)
                        + "]\n"
                    )
                    temp = temp.next
            string = string + "}"
        print(string)
            
if __name__ == "__main__":
    V = 5
    g = Graph(V,"undirected") 
    g.add_edge(0, 1, 7) 
    g.add_edge(0, 4, 7) 
    g.add_edge(1, 2, 7) 
    g.add_edge(1, 3, 7) 
    g.add_edge(1, 4, 7) 
    g.add_edge(2, 3, 7) 
    g.add_edge(3, 4, 7) 
  
    g.export_graphviz()