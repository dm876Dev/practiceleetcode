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






#With graphs, you either traverse them using DFS or BFS 


#Recursive DFS Tree Template
def dfs(root):
    if root is None:
        return

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
