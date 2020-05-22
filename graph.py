# -*- coding: utf-8 -*-

#Undirected graph with edge costs implementation. Includes graphviz format export functionality.

class AdjacencyListCell:
    """
    Basic building block of the adjacency lists for each graph vertex. 
    Essentially contains each directed edge in the graph and its metadata.
    
    Undirected edges are equivalent to two directed ones, one on each of the 
    two connected vertices. They are automatically added depending on the 
    graph type
    """
    
    def __init__(self,adjacent_vertex_id: int,edge_cost: float,next: 'AdjacencyListCell') -> None:
        """
        AdjacencyListCell constructor.

        Parameters
        ----------
        adjacent_vertex_id : int
            Id of the adjacent vertex in the vertex_adjacency_lists list.
        edge_cost : float
            Assigned cost of the edge that connects to the adjacent vertex.
        next : 'AdjacencyListCell'
            Contains the whole object that represents the next edge in the 
            adjacency list. What this means is that the elements of the 
            vertex_adjacency_lists list are single AdjacencyListCells that 
            contain another AdjacencyListCell inside this variable, which also 
            contains another AdjacencyListCell, and so on.

        Returns
        -------
        None

        """
        self.id = adjacent_vertex_id
        self.cost = edge_cost
        self.next = next

class Graph:
    """
    Class representing the whole graph including all its vertices, edges, and 
    the edge costs.
    
    The graph is implemented using adjacency lists.
    """
    
    def __init__(self,vertex_number: int,type: str="directed") -> None:
        """
        Graph constructor.

        Parameters
        ----------
        vertex_number : int
            Number of all graph vertices.
        type : str, optional
            Can only be "directed" or "undirected". The default is "directed".
            
            Directed graphs allow traversing at least one of their edges from 
            one side only.
            
            Undirected graphs allow traversing all edges from both sides.
            Undirected edges are implemented by using 2 opposite directed 
            edges.

        Raises
        ------
        ValueError
            When the given type is not "directed" or "undirected"

        Returns
        -------
        None.

        """
        
        #type check
        valid_types = {"directed","undirected"}
        if type not in valid_types:
            raise ValueError("type must be one of %r." % valid_types)
        
        self.type = type
        self.vertex_number = vertex_number
        self.vertex_adjacency_lists = [None] * self.vertex_number
        
    def add_edge(self,src: int,dest: int,cost: float) -> None:    
        """
        Creates a directed edge by adding an AdjacencyListCell object to src's 
        adjacency list.
        
        If the graph's type is "undirected", also adds the opposite directed 
        edge.

        Parameters
        ----------
        src : int
            Edge starts from here.
        dest : int
            Edge goes here.
        cost : float
            An edge's cost is simply an assigned numeric value that symbolises 
            the abstract "cost" of traversing from src to dest.

        Returns
        -------
        None.

        """
        
        #prepend dest's index to src's adjacency list
        self.vertex_adjacency_lists[src] = AdjacencyListCell(dest,cost,self.vertex_adjacency_lists[src])
        
        if self.type == "undirected":
            #prepend src's index to dest's adjacency list (for undirected graphs)
            self.vertex_adjacency_lists[dest] = AdjacencyListCell(src,cost,self.vertex_adjacency_lists[dest])
        
    def print_graph(self) -> None: 
        """
        Prints the graph in a human-readable format.
        
        Not recommended for large graphs.

        Returns
        -------
        None

        """
        
        print("<vertex>: <reachable vertex>(<edge cost>), ...")
        
        for i in range(self.vertex_number): 
            print("v{}: ".format(i), end="") 
            temp = self.vertex_adjacency_lists[i] 
            while temp: 
                print("v{}({})".format(temp.id,temp.cost), end="") 
                temp = temp.next
                if temp: print(",",end="")
            print(" \n",end="")
            
    def export_graphviz(self) -> str:
        """
        Creates a string containing the graph in graphviz's format (named DOT). 
        Can be used with python graphviz libraries or webgraphviz to visualise 
        a graph. Visualise large graphs at your own risk.

        Returns
        -------
        str
            A string with the graph in DOT format

        """
        
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
            
        elif self.type == "undirected":
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
            
        return string

#small demo script
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
  
    print(g.export_graphviz())