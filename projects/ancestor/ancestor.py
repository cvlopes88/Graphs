from util import Stack, Queue
from graph import Graph




def earliest_ancestor(ancestors, starting_node):
    
    # import graph class 
    graph = Graph()
    
    # Create a queue
    q = Queue()
    # Enqueue the starting vertex
    q.enqueue(starting_node)
    # Create a set to store visited vertices
    visited = set()
    # While the queue is not empty...
    while q.size() > 0:
        # Dequeue the first vertex
        v = q.dequeue()
        # Check if it's been visited
        # If it hasn't been visited...
        if v not in visited:
            # Mark it as visited
            print(v)
            visited.add(v)
            # Enqueue all it's neighbors
            for neighbor in graph.get_neighbors(v):
                print("printing neighbor>>>", neighbor)
                q.enqueue(neighbor)
                break
    else:
        print("didnt find shit")
        

