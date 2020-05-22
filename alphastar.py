# -*- coding: utf-8 -*-
import graph
import heapq
import collections
from typing import List,Deque

def Astar(graph: graph.Graph,start: int,dest: int,heuristic_scores: List[float]) -> Deque[int]:
    """    
    Implementation of the A* shortest path algorithm.

    Parameters
    ----------
    graph :  graph.Graph
        Custom object containing the graph to perform the search on. (separate 
        graph module required)
    start : int
        Starting vertex's index in the Graph's vertex_adjacency_lists list.
    dest : int
        Target vertex's index in the Graph's vertex_adjacency_lists list.
    heuristic_scores : List[float]
        List containing heuristic values for each vertex in the 
        vertex_adjacency_lists list.

    Raises
    ------
    ValueError
        When the amount of heuristic values in the heuristic scores array does 
        not match the number of vertices on the given graph.
    Exception
        When no path to the target vertex was found.

    Returns
    -------
    Deque[int] (collections.deque)
        Deque of the indices of the vertices that form the complete path found 
        by the A* algorithm from start to finish. 

    """
    
    class FrontierVertex:
        """Object containing the vertex index and the related metadata of 
        vertices in the "frontier" or "open set" of the algorithm
        
        Packaging every frontier vertex in this object allows for easy access 
        of its metadata such as the accumulated cost of the path up to that 
        vertex and its f score
        """
        def __init__(self,id: int,g: float,previous_vertex: 'FrontierVertex') -> None:
            """
            FrontierVertex contructor.

            Parameters
            ----------
            id : int
                Vertex's index in the Graph's vertex_adjacency_lists list.
            g : float
                Accumulated cost of the path that led to this vertex.
            previous_vertex : 'FrontierVertex'
                The vertex object from which this vertex was explored by the 
                algorithm.

            Returns
            -------
            None.

            """
            
            self.id = id
            self.g = g
            self.previous_vertex = previous_vertex
            
            """
            f score of the vertex is calculated as the sum of g and the 
            heuristic value of the vertex'
            """
            self.f = g + heuristic_scores[self.id]
            
        def __eq__(self,id: int) -> bool:
            """
            Custom equality operator.
            
            Necessary for the direct comparison of vertex id's (integers) with 
            the id of the FrontierVertex object.
            
            Indirectly also enables usage of the "in" and "not in" operators 
            as such:
                if (neighbour_vertex_id not in frontier ...
            (where frontier is an iterable with FrontierVertex objects)

            Parameters
            ----------
            id : int
                Vertex's index (to be compared to the FrontierVertex object's 
                index) in the Graph's vertex_adjacency_lists list.

            Returns
            -------
            bool
                True if equal, false if not.

            """
            
            return self.id == id
            
        def __lt__(self,other: 'FrontierVertex') -> bool:
            """
            Overridden "<" operator.
            
            Allows for utilisation of the automatic sorting provided by the 
            heapq data structure used for the frontier.

            Parameters
            ----------
            other : FrontierVertex
                Another FrontierVertex object.

            Returns
            -------
            bool
                True if this vertex has a lower f score than the other, false 
                otherwise.

            """
            
            return self.f < other.f
        
        def __repr__(self) -> str:
            """
            Overridden representation operator.

            Returns
            -------
            str
                A nicely formatted string with the vortex's name and f score.

            """
            
            return "v" + str(self.id) + "(" + str(self.f) + ")"

        def retrace_from_here(self) -> Deque[int]:
            """
            Algorithm subroutine that reconstructs the path that led to this 
            vertex and returns it.
    
            Returns
            -------
            Deque[int] (collections.deque)
                Deque containing the path's vertices' indices from start to 
                finish.
    
            """
            
            #initialisation of empty queue
            path = collections.deque([])
            
            current = self
            
            """
            walk backwards on the path of vertices that led to this vertex and 
            append each of their indices to the front of the queue.
            """
            while current != start:
                path.appendleft(current.id)
                current = current.previous_vertex
                
            #finally also append the starting vertex's index
            path.appendleft(start)
            
            return path
    
    def explore_frontier_cheapest_vertex() -> None:
        """
        Algorithm subroutine that removes the vertex with the lowest f score 
        from the frontier and adds its newly discovered adjacent vertices.
        
        A min-heap is a data structure that remains sorted with every element 
        addition or removal.
        
        Popping the heap means removing the element at its first position.
        
        Due to modifications of the __lt__ operator of the FrontierVertex 
        objects, the vertices in the frontier min-heap are sorted according to 
        f score. Therefore, the one popped is always the vertex with the 
        lowest f score in the frontier.

        Returns
        -------
        None

        """
        
        #vertex with lowest f score is popped from the frontier min-heap
        explored_vertex = heapq.heappop(frontier)
        
        """
        the vertex's adjacency list in the Graph object is accessed 
        and all adjacent vertices not already in the frontier are inserted 
        into the frontier (excluding the vertex itself)
        """
        temp = graph.vertex_adjacency_lists[explored_vertex.id]
        while temp:
            neighbour_vertex_id = temp.id
            edge_cost = temp.cost
            
            """
            the check "neighbour_vertex_id not in frontier" is made possible 
            due to the custom __eq__ operator of FrontierVertex objects
            """
            if (neighbour_vertex_id not in frontier 
                and neighbour_vertex_id != explored_vertex.id):
                
                heapq.heappush(frontier,
                               FrontierVertex(neighbour_vertex_id,
                                              explored_vertex.g + edge_cost,
                                              explored_vertex)
                               )
                
            temp = temp.next
            
    if len(heuristic_scores) != graph.vertex_number:
            raise ValueError("the amount of heuristic values in the heuristic \
                             scores array does not match the number of \
                                 vertices on the given graph")
    
    #min-heaps need to be initialised as empty lists
    frontier = []
    
    """
    by adding the starting vertex, the list is automatically also converted 
    to a min-heap
    """
    heapq.heappush(frontier,FrontierVertex(start,0,None))
    
    #as long as the frontier still contains vertices...
    while frontier:
        if frontier[0] == dest:
            """
            The first element (index 0) of the min-heap is always the "min", i.e. 
            the vertex with the lowest f score.
            
            If the target vertex is in the frontier with the lowest f score, then 
            that means that there is not a possibly better path to it. Time to 
            reconstruct and return the path that led here to get the shortest path 
            from the starting to the target vertex.
            """            
            return frontier[0].retrace_from_here()
        else:
            """
            Until the target vertex ends up in the frontier AND there is no 
            faster way to it, the algorithm will keep trying to "explore" 
            vertices in the frontier. Then they are removed from the frontier 
            and the vertices adjacent to them are added. The order in which 
            the frontier vertices are explored is decided by their f score.
            """
            explore_frontier_cheapest_vertex()
    
    raise Exception("Destination unreachable")

#simple test script for demonstration purposes
if __name__ == "__main__":

    #https://en.wikipedia.org/wiki/File:AstarExampleEn.gif
    #a-0, b-1, c-2, d-3, e-4, f-5
    testgraph = graph.Graph(7,"undirected")
    heuristics = [4, 2, 4, 4.5, 2, 0, 5]
    testgraph.add_edge(0,1,2)
    testgraph.add_edge(1,2,3)
    testgraph.add_edge(0,6,1.5)
    testgraph.add_edge(6,3,2)
    testgraph.add_edge(3,4,3)
    testgraph.add_edge(4,5,2)
    testgraph.add_edge(2,5,4)
    
    print(testgraph.export_graphviz())
    
    print(Astar(testgraph,6,5,heuristics))
    