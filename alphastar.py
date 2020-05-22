# -*- coding: utf-8 -*-
import graph
import heapq
import collections

def Astar(graph,start,dest,heuristic_scores):
    if len(heuristic_scores) != graph.vertex_number:
            raise ValueError("the amount of heuristic values in the heuristic scores array does not match the number of vertices on the given graph")
    
    frontier = []
    
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
            
        path.appendleft(start)
        
    
    heapq.heappush(frontier,FrontierVertex(start,0,None))
    
    def explore_frontier_cheapest_vertex():
        explored_vertex = heapq.heappop(frontier)
        
        temp = graph.vertex_adjacency_lists[explored_vertex.id]
        while temp:
            neighbour_vertex_id = temp.id
            edge_cost = temp.cost
            
            if (neighbour_vertex_id not in frontier and neighbour_vertex_id != explored_vertex.id):
                print(neighbour_vertex_id)
                heapq.heappush(frontier,FrontierVertex(neighbour_vertex_id,explored_vertex.g + edge_cost,explored_vertex))
                
            temp = temp.next

if __name__ == "__main__":
    V = 5
    mygraph = graph.Graph(V,"undirected")
    mygraph.add_edge(0, 1, 1)
    mygraph.add_edge(0, 4, 1)
    mygraph.add_edge(1, 2, 1)
    mygraph.add_edge(1, 3, 1)
    mygraph.add_edge(1, 4, 1)
    mygraph.add_edge(2, 3, 1)
    mygraph.add_edge(3, 4, 1)
    #mygraph.export_graphviz()
    
    import array
    heuristics = array.array("i",[0] * V)
    Astar(mygraph,0,3,heuristics)