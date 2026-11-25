# BFS = FIFO: First In, First Out.
# popleft() = Removes the first (leftmost) node.
# append() = Adds a node to the end (right side).
# Level by level: BFS explores the tree from top to bottom, one level at a time.
# Use BFS for: Finding a target, exploring levels/depths, or finding the closest node (fewest edges away).

def bfs(root):
    queue = deque([root])        # Start with the root node and add it to the deque (queue).

    while len(queue) > 0:        # Keep looping while the queue isn't empty.
        node = queue.popleft()   # Remove and return the first node from the queue (FIFO), storing it in current node

        for child in node.children:  # Go through each child of the current node.
            if is_goal(child):       # Check if the child is the target node.
                return FOUND(child)  # Return if the goal is found.

            queue.append(child)      # Otherwise, add the child to the end of the queue.

    return NOT_FOUND             # Return NOT_FOUND if the goal wasn't found after exploring the tree.








#BFS for Trees Syntax
from collections import deque 

def bfs_trees(root):
    queue = deque(root, target) #allows us to remove the frontstarting with the root
    while len(queue) > 0: #while the queue is not empty(exists)
        node = queue.popleft() #pop from leftside storing what is returned into node
        for child in node.children: #for any child amongst the node's children
            if child.val == target: #if child's value is our = target return
                return child 
            queue.append(child) #if not, append 
    return -1 #or None #if node is not matching target  

result = bfs(root, 5) #Call BFS and set the target to 5, KEEP root
return result #or just combine both, return bfs(root, 5)

#function_name(argument 1, argment 2)

#It keeps going until target is found -> returns child
#If target isnt found, keeps going and exploring allnodes
#If all nodes have beenr eached, and no target found retunrn None or return -1




#BFS for Graphs Syntax
#Allows for circles, loops, mutliple conecions between nodes
#To prevent redunat work like viisitng same node once or inifite looop, vfs must track visited nodes

#Start with root node and visited set. 
# While queue isn't empty. Loop through current node's neighbors. 
# If neighbor is visited, skip it (continue). 
# Otherwise, mark as visited and add to queue.

from collections import deque

def bfs_graphs(root):
    queue = deque([root])          # Create a deque (queue) and add the starting node.
    visited = set([root])          # Create a set to track visited nodes, starting with root.

    while len(queue) > 0:           # Keep looping while the queue isn't empty.
        node = queue.popleft()      # Remove and return the first node from the queue.

        for neighbor in get_neighbors[graph, node]: # Loop through all neighbors connected to the current node. get_neigbors is a helper fucntion
            if neighbor in visited:  # Check if the neighbor has already been visited.
                continue             # Skip this neighbor and move to the next one.

            visited.add(neighbor)    # Mark the neighbor as visited to prevent revisiting.
            queue.append(neighbor)   # Add the neighbor to the back of the queue.

    return visited                  # Return all nodes visited during BFS.
          
def get_neighbors(graph, node): #helper funciton 
    return graph[node] #Return all neighbors connected to the current node.
  
# Use when working with grids, adjaceny lists, or networks
# Structure cna continas cycles or duplicate paths
# find shortest num of steps or min loops
# explore possivle states(games, logic problems)

# use ful when all edges or modes have same cost bc it will find shortest path first
# trees and graphss followstrucutre of 1. a queue to allow for explroation of nodes level by elvel
# 2. a loop to processes each node
# 3. a branching step where ndoes are added to queue

#DFS TREE
def dfs(root, target):
    if root == None:
      return Non
      if root.val == target:
        return root
      left = dfs(root.left, target) #calls DFS recursivelesly on left child of curent node, to look for target (searches left subtree)
      if left is not None
          return left
      return dfs() #calls DFS recursively on right child (searches right subtree)

#DFS GRAPH

def get_neighbors(graph, node): #helper funciton 
    return graph[node] #Return all neighbors connected to the current node. #usually dicitoanry so vlaues asociated with colummn are the neighbors

def get_neighbords(graph, node)
    return graph[node] #so looks up the node in dictioanry and reutrns its asociated value(neighbor)








