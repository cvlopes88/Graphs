import random
from util import Queue


def find_unexplored(room):
  
    unexplored = [dir for dir in room if room[dir] == '?']
    print("unexplored", unexplored)
    if len(unexplored) == 0:
        return None
    direction = unexplored[random.randint(0, len(unexplored) - 1)]
    print("*****", direction)
    return direction


def find_direction(current_room, target_room_id):
    for direction in current_room:
        if current_room[direction] == target_room_id:
            return direction
    return None
  

def visit_all_rooms(player):

    path = []
    graph = {}
    starting_room = player.current_room.id
    unexplored_room = 0  
    
    graph[starting_room] = {}
    for i in player.current_room.get_exits():
      graph[starting_room][i] = '?'
      unexplored_room += 1
      
      reverse_directions = {'n': 's', 's': 'n', 'e': 'w', 'w': 'e'}
      
      # While there's unexplored rooms in the graph
      while unexplored_room > 0:
        # print("unexplored>>", unexplored_room)
        current_room = player.current_room.id
        # Check if current room have unexplored path
        if '?' in graph[current_room].values():
          
          print("find the ?", graph[current_room].values())
          #if yes, find unexplored direction from current room
          direction = find_unexplored(graph[current_room]) 
          # Move in that direction
          player.travel(direction)
          next_room = player.current_room.id
          path.append(direction)
          # Add that direction to graph replace '?' 
          graph[current_room][direction] = player.current_room.id
          if not next_room in graph:
            graph[next_room] = {}
            for a in player.current_room.get_exits():
              graph[next_room][a] = '?'
              unexplored_room += 1
          graph[next_room][reverse_directions[direction]] = current_room
          unexplored_room -= 2
      else:
          # if no paths left,
          # perform a bfs to find nearest room with unexplored path ('?')
          # Create queue
          q = Queue()
          # Enqueue a path to starting room
          q.enqueue([current_room])
          # Create a set to store all visited rooms
          visited = set()
          # While queue is not empty...
          while q.size() > 0:
              # Dequeue the path
              p = q.dequeue()
              # Grab last room
              room = p[-1]
              
              direction = find_unexplored(graph[room])
              
              # Check if room has unexplored exists
              if direction is not None:
                # if so convert room id in path direction
                for i in range(len(p) - 1):
                  d = find_direction(graph[p[i]], p[i + 1])
                  print("##########>>", d)
                  # Add to traversal path
                  path.append(d)
                  # Move player
                  player.travel(d)
                  # Break Loop
                break
                  
              # Check if it has been visited if noy..
              if room not in visited:
                  # Mark it as visited
                  print("Getting Visited>>>", room)
                  visited.add(room)
                  # Enqueue all its neighbors
                  for e in graph[room]:
                    visited_copy = p.copy()
                    visited_copy.append(graph[room][e])
                    q.enqueue(visited_copy)
                    print("visited copy>>>", visited_copy)
                    
    return path
