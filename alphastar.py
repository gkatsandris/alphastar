# -*- coding: utf-8 -*-
import graph
import heapq
import collections

def Astar(graph:graph.Graph,start:int,dest:int,heuristic_scores):
    class FrontierVertex:
        def __init__(self,id,g,previous_vertex):
            self.id = id
            self.g = g
            self.f = g + heuristic_scores[self.id]
            self.previous_vertex = previous_vertex
            
        def __eq__(self,id):
            return self.id == id
            
        def __lt__(self,other):
            return self.f < other.f
        
        def __repr__(self):
            return "v" + str(self.id) + "(" + str(self.f) + ")"

    def retrace_from(vertex):
        path = collections.deque([])
        
        current = vertex
        while current != start:
            path.appendleft(current.id)
            current = current.previous_vertex
            
        path.appendleft(start)
        
        return path
    
    def explore_frontier_cheapest_vertex():
        explored_vertex = heapq.heappop(frontier)
        
        temp = graph.vertex_adjacency_lists[explored_vertex.id]
        while temp:
            neighbour_vertex_id = temp.id
            edge_cost = temp.cost
            
            if (neighbour_vertex_id not in frontier and neighbour_vertex_id != explored_vertex.id):
                heapq.heappush(frontier,FrontierVertex(neighbour_vertex_id,explored_vertex.g + edge_cost,explored_vertex))
                
            temp = temp.next
            
    if len(heuristic_scores) != graph.vertex_number:
            raise ValueError("the amount of heuristic values in the heuristic scores array does not match the number of vertices on the given graph")
    
    frontier = []
    heapq.heappush(frontier,FrontierVertex(start,0,None))
    
    while frontier:
        if frontier[0] == dest:
            return retrace_from(frontier[0])
        else:
            explore_frontier_cheapest_vertex()
    
    raise Exception("Destination unreachable")

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
    testgraph.export_graphviz()
    
    print(Astar(testgraph,6,5,heuristics))
    