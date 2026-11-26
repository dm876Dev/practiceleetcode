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
# trees and graphss followstrucutre of 



njjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj
#jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj



#DFS TREES recursively
def dfs(root):
    if root is None:
        return

    # Process current node.

    dfs(root.left)   # Explore left subtree.
    dfs(root.right)


#DFS TREES with a targrt
def dfs(root, target):
    if root == None:
        return None

    if root.val == target:
        return root

    left = dfs(root.left, target)
    # Calls DFS recursively on the left child to search for the target.

    if left is not None:
        return left

    return dfs(root.right, target)
    # Calls DFS recursively on the right child.

#DFS GRAPH

def get_neighbors(graph, node): #helper funciton 
    return graph[node] #Return all neighbors connected to the current node. #usually dicitoanry so vlaues asociated with colummn are the neighbors

def get_neighbords(graph, node)
    return graph[node] #so looks up the node in dictioanry and reutrns its asociated value(neighbor)




# 1. Recursive DFS Tree
# 2. Recursive DFS Graph
# 3. Iterative BFS Tree
# 4. Iterative BFS Graph
# 5. Iterative DFS (stack)
#DFS usuall (E + V) :num of edges and nodes, its cells that are connected n^2 worst, Space: O(N^2)





#With graphs, you either traverse them using DFS or BFS 


#Recursive DFS Tree Template
def dfs(root):
    if root is None:
        return 0

    dfs(root.left)
    dfs(root.right)


#Solution LC- 104 Maximum Depth of Binary Tree:
#Find the longest path from the root to the leaf node, along the path we're coutning then umber of nodes as the depth
#count the root as 1, return max of left and right subtrees plus 1, so break it into subproblems, search max step of left subtree and right
#ex 1 , count our root node as 1, search the left subtree recursively call max depth we return is 1(1 level), search our right subtree recursively call max depth return is 2(2 levels), go back up to the root and form the perspective of the root, we return 1 + max of left and right max is 2, so we return 3(1+2)
#DF Tree T: O(N) S:O(N) worst case  because we go through entire tree!

def maxDepth(root, self):
    if root is None:
        return 0  # If no root node exists, depth is 0.

    left = self.maxDepth(root.left)    # Find depth of left subtree recursively(looks at max depth of the roots left child).
    right = self.maxDepth(root.right)  # Find depth of right subtree recursively(looks at max depth of the roots right child).

    return 1 + max(left, right)   # Add current node to the greater depth (max subtree's depth of both of the subtrees)


# Your original DFS Tree template + these additions:
# 1. return 0 → base case for an empty node.
# 2. left = dfs(root.left) → save left subtree result.
# 3. right = dfs(root.right) → save right subtree result.
# 4. return 1 + max(left, right) → return the greater depth + current node.
#New Syntax: max(a, b) return the greater value of the two; # 1 +  count the first node; left variablethat's  stored left subtree, right < variable that's stored right subtree



#Iterative DFS Tree Template (Non-Recursive)
#insteead of recursion use a stack , implement preorder traversal dfs with a stack, bc its easiest (Current (Root)) → visit all the Left until it cant→ the Right -> redoes process of left then right)  first process root node, then goes as left as possible, then goes to the right child and starts over so keeps going leftwards until it cant....)
def dfs_tree(root):
    stack = [root]  # Start with root in the stack.

    while stack:
        node = stack.pop()  # Pop the most recently added node, and stores it in node

        if node.left: #checks whether the current node has a left child
            stack.append(node.left) #if it does, add the left child to the stack 

        if node.right: #checks if current node has a right child
            stack.append(node.right) #if it does, add the right child to the stack


#Solution to leetcode:
def dfs_tree(self, root): #preorder traversal

    if root is None: #if no root root node exists, then we return 0, exit the function
        return 0
        
    stack = [[root, 1]]  # Create a stack that stores current node and the depth of each node. Root, its depth is 1
    result = 1 #tracks out maximum depth, we know its at least 1 cus we stored the root, we can later update it
    
    while stack: #While stack is not empty
        node, depth = stack.pop()  # Pop 2 values (the most recently added node, and its depth)
        if node: #If node exists
            result = max(result, depth) #update our result with the maximum between the previous node's depth and the current node's depth 
            stack.append(node.left, depth + 1) #add left children to the stack and increment the depth
            stack.append(node.right, depth + 1) #add right children to the stack and increment the depth 
    #Keeping traversing the tree until the stack is empty 
    return result 
    
# Stack stores the current node and its depth.
# Pop the most recently added node and retrieve the node and its depth.
#   udating our result throughout
# Push(append) current node's left and right children onto the stack with depth + 1.
# Continue until the stack is empty, then return the maximum depth.

#Trees are acyciclal so we dont need to worry whether the same node been visited vs for graphs, we must keep track of marking the node


#DFS Graph recursive 
def dfs_graph(graph, node, visited):
    if node in visited: #if node already visited, stop exploring the graph
        return 0

    visited.add(node) # mark current node as visited

    for neighbor in graph[node]: #for each neighbor in the graph -check all the neighbors
        if neighbor not in visited: #if the neighbor has not been visited
            self.dfs_graph(graph, neighbor, visited) #explore recursively

#DFs Graph Iterative 
class Solution:
    def dfs_graph(self, graph, root, visited):

        stack = [root]  # Start with the starting node.
        visited.add(root)  # Mark it as visited.

        while stack:  # While stack is not empty.
            node = stack.pop()  # Remove the most recently added node store it as node

            for neighbor in graph[node]:  # Check all neighbors
                if neighbor in visited: #if already visited
                    continue  # Skip the node and keep going 
                visited.add(neighbor)  # Mark neighbor as visited
                stack.append(neighbor)  # Append/add neighbor to the stack

#DF TREE VS GRAPH: trees have a built-in structure (left and right children), while graphs have connections (neighbors) that can form cycles.
#Needs visited to prevent revisiting nodes and getting stuck in cycles
#Explores all connected neighbors

#547 Number of Provinces
#Given: a -> b , b-> c , a->c indirectly, "isConnected[i][j] is 1 or 0" at the end means its a adjancy matrix which shows whether each pair of nodes is connected 1 is if connected, 2 is if not
#Vocab: group of conencteed cities is called a province
#Goal: return the total num of provinces, so looking for a set of connected components

# Strategy: Use DFS to find all connected components (provinces).
# Core idea: Keep track of visited nodes using a set and maintain a running count of provinces.
# Loop through each node: if already visited, skip it because it belongs to a connected component (province) we already explored.
# If not, increment our province count(BEFORE starting DFS)
# And start DFS to visit all connected nodes, updating visited.
# Continue our loop until connected components all visited, and return the count

# For example, we have these connected components rep our provinces: 
# 1-2, 3-4-5, 6
# start at node 1 and explore that component (2) with DFS
# there no more unvisited nodes, increment province count by 1, then we and start loop over, skipping 2. 

# start at node 3 and explore nodes 3, 4, and 5.
# Once DFS finishes, increment our province count by 1.
# Go back to the loop: it skip nodes 4 and 5 because they're already visited.
# If we reach node 6 and it hasn't been visited, start another DFS 

# Check all nodes connected to 6, then increment our count by 1.
# All nodes have been checked, return connected component count: 3

#Recursive: first write everything skipping the helper then after count before the for loop add the helper function(at the top

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        n = len(isConnected)  # Get number of nodes
        visited = set()       # Keep track of visited nodes
        count_of_provinces = 0

        # DFS helper function
        def dfs(i):
            visited.add(i)  # BASE CASE(stopping condition): when we visit a node, add it to visited set, prevents us from revisiting the same node and be stuck in a loop
            for j in range(n): # Go through neighbors and check which nodes are connected.
                if j not in visited and isConnected[i][j] == 1:
                    dfs(j)  # Recursive call: explore connected node j

        for i in range(n): # Go through every node (0 to n-1)
            if i not in visited:
                dfs(i)
                count_of_provinces += 1

        return count_of_provinces


#Instead of recursively calling DFS on each connected, unvisited node, we add it to the stack. 
#We keep popping (removing) nodes and pushing (adding) their unvisited neighbors until the stack is empty.


#Iterative DFS on Graph:
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)  # Get number of nodes.
        visited = set()       # Keep track of visited nodes.
        count_of_provinces = 0

        for i in range(n):    # Go through every node (0 to n-1).
            if i not in visited:
                stack = [i]   # Start stack with the current node.
                visited.add(i)

                while stack:  # While stack is not empty.
                    node = stack.pop()  # Remove most recently added node.

                    for j in range(n):  # Check every possible neighbor.
                        if j not in visited and isConnected[node][j] == 1:
                            visited.add(j)  # Mark neighbor as visited.
                            stack.append(j) # Add neighbor to stack.

                count_of_provinces += 1  # Finished exploring one province.

        return count_of_provinces
 

# Leetcode 200: Number of Islands
# It's an adjacency matrix (2D grid of rows and columns): "1" = land, "0" = water.

# Higher-level big idea:
# - Find an unvisited "1" → increment island count.
# - DFS explores all connected "1"s all 4 directions(up, down, left, right), marking them visited (4 direction check)
# If it finds an unvisited "1" , it recursively moves to that cell and repeats the same check
# - Stop when there are no more connected land cells
# Keep scanning for another unvisited "1" ignoring the water "Os" → count the "1" as a new island, and repeats recursion
# - Return the total number of islands.


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        m = len(grid)  # Get number of rows
        n = len(grid) #get number of columns
        visited = set()       # Keep track of visited nodes.
        count_of_islands = 0
                
        # DFS helper function
        def dfs(r, c):  # Explore connected land starting from the current cell's coordinates (row and column).
            visited.add((r, c))  # Mark current cell as visited.
        
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Define the four directions we can move: right, left, down, up.
        
            for off_r, off_c in directions:  # Find the four neighboring cells (coordinates) around our current cell.
                nr = r + off_r  # Calculate the neighbor's row coordinate by adding the row offset.
                nc = c + off_c  # Calculate the neighbor's column coordinate by adding the column offset.
        
                # Some if checks to see if the neighbor is valid, land, and unvisited.
                if (0 <= nr < m and 0 <= nc < n  # Check if the neighbor's row and column are within the grid boundaries.
                    and grid[nr][nc] == "1"  # Check if it's land.
                    and (nr, nc) not in visited):  # Check if it hasn't been visited.
                    dfs(nr, nc)  # If it passes all those checks, recursively explore the next connected neighbor.
        
        # Go through every cell in the grid(all the rows and columns) if the current cell is land and hasn't been visited
        #start DFS to explore its connected land cells, then increment the island count by 1.
        for r in range(m):
            for c in range(n):
                if grid[r][c] == "1" and (r, c) not in visited:
                    dfs(r, c)
                    count_of_islands += 1

        return count_of_islands #return the count

# Keep track of visited cells and the running count of islands.
# Define a recursive DFS helper function to explore connected land cells
# Define the four directions to check around the current cell (right, left, down, up).
# Inner for loop: goes through each direction to get the row and column offsets for the neighboring cell
# If statment checks if the neighboring cell is within the grid, is land ("1"), and hasn't been visited.
# If valid, recursively call DFS to explore the connected neighbor until there are no more 
# Outer for loops scan the entire grid for unvisited "1" cells.
# When an unvisited "1" is found, start DFS to explore its entire island.
# Once DFS finishes exploring that island, increment the island count by 1.
# Continue scanning the grid for more unvisited "1" cells.
# Return the total number of islands.



#DF Iteratively: With a stack (instead of recursive call) and visited set(bc graph, trees not)
#Find an unvisited "1" (land) cell, ignoring the "0" water cells, and make visited set, make a stack to explore all 
#connected neighboring cells horizontally and vertically) until the stack is empty, that would mean 
#one complete island has been explored and visited, and we'd increment the island count
# and we'd restart the process and search for the next unvisited "1" (land) cell
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        m = len(grid)  # Get number of rows
        n = len(grid) #get number of columns
        visited = set()  # Keep track of visited nodes.
        count_of_islands = 0
        
        # Go through every cell in the grid(all the rows and columns) if the current cell is land and hasn't been visited
        for r in range(m): #outer loop scans entire grid
            for c in range(n):
                if grid[r][c] == "1" and (r, c) not in visited: #checks for if the current cell is land and hasn't been visited
                    stack = [(r, c)] #Start a stack with current land cells coordinates(#rows, #columns
                    visited.add((r, c))  # Mark current cell as visited.
        

            while stack: #while stack is not empty
                r, c = stack.pop() #remove the most recently aded cell to explore it
                directions = [(0, 1), (0, -1), (1, 0), (-1, 0)] #heres are the 4 directions we can move 
                #same row move 1 right, one left, 1 row down/up, same column
            
            #Find the 4 neighbor cells(coordinates of):    
            for off_r, off_c in directions:  #go through each of the four directions, getting the row offset (off_r) and column offset (off_c) for each one.
                nr = r + off_r  # get the neighbor's row coordinate by adding the row offset to current cells row
                nc = c + off_c  # get the neighbor's column coordinate by adding the column offset to current cells column
            
                # Some if checks to see if the neighboring cell is within the grid, is land, and hasn't been visited.
                if (0 <= nr < m and 0 <= nc < n  # Check if the neighbor's row and column are within the grid boundaries.
                    and grid[nr][nc] == "1"  # Check if it's land.
                    and (nr, nc) not in visited):  # Check if it hasn't been visited.
                    
                    # Add valid neighbors: Mark the neighbor as visited and add its coordinates to the stack.
                    visited.add((nr, nc))
                    stack.append((nr, nc))
                        
            count_of_island += 1  #increment the count after the stack is empty to add a new island; continue scanning the grid.
            
        return count_of_islands #return the count

# Keep track of visited nodes and running count of islands
# Enter outer for loop: scaning the entire grid, find an unvisited "1" (new island)
# if statement confirms its land and unvisited
# Initialize stack: Add its coordinates and mark it visited (so our stack stores connected 1 cells that need to be explored)
# Inner while loop: Pop cells from the stack and check their four neighbors until the stack is empty.
# Find the neighbors of the current cell, in 4 directions(adding the offset to original row or column, to get new coordinates of the neighbor cell)
# Check if the neighbor is valid(within the grid coordinates), land, and unvisited
# Mark the neighbor as visited and add its coordinates to the stack.
# once the stack is empty, one complete island has been explored, increment the count. 
# outer for loop resumes, continue scanning for unvisted "1"s
# Return the total number of islands at the end

#BFS
#https://www.youtube.com/watch?v=2aA0JfkOCD4

#BFS Tree Template

#BFS Graph Template











