#DFS with bility to reverse a choice
#sudoko solver, word search, subset ans permutation, containt based problems like n queens, combinations



#recursive dfs
#base case is leaf means reached solution, store copy of path if we didnt wed overwigte all our answers
#each step try all valid next choices or edges from current case #slicing next string, etc
#prune early, if option breaks contraint skip it, faster the backtracking finsihes 
#[ath.add(edge)
#update stuff updating 
#dfs recursive call
#revert() undo decision made


#Backtracking template

def backtracking(self, n: int) -> List[str]:
  ans = [] #empty list
  
  def dfs(start_index, path, [...additional states]):
#base case is leaf means reached solution, store copy of path otherwise we'd overwrite all our answers
      if is_leaf(start_index):
          ans.append(path[:])  # Add a copy of the path to the result.
          return
   #each step try all valid next choices or edges from current case
      for edge in get_edges(start_index, [...additional states]):
        
          # Prune if needed
          if not is_valid(edge):
              continue
  
          path.add(edge)
          #update stuff
          if additional_states:
              update([...additional states])
  
          dfs(start_index + len(edge), path, [...additional states])
  
          # Revert additional states if necessary, e.g. permutations
          path.pop()
        
#22. Generate Parentheses Solutions- 

# Big idea:
# Build all valid combinations one parenthesis at a time.
# Only make choices that keep the combination valid.
# Backtrack to undo a choice and try the other option.
# Strategy: Backtracking, with recursion and a path(store current combination we're building) to add to our result of all combinations
#Backtracking, you make a choice and explore it recursively, undo your last choice to allow trying others
Brute force brainstorming: 
# Ex 1: n = number of pairs. n = 3 means theres 3 "(" open and 3 ")" closed parenthesis
-> Base case: open == closed == n, this is a complete combination we must return 0/None 
# the order matter's: the open ( of the pair, must come before its closed counterpar to a valid combot, so it must be greater in the count so far
->2 counts: open_count, close_count
-> Add "(" if open_count < n (can't exceed n pairs)
-> Add ")" if close_count < open_count (must have a matching "(" first).
#    Example: ")(" is invalid.

#Pseudo code:
FUNCTION generateParenthesis(n)
    results = [] #list of all completed valid parenthesis combinations

    # BACKTRACK helper to build valid parentheses combinations
    FUNCTION backtrack(path, open, closed) #path tracking the current combination being built, #open and closed parethesis counts

        # Base case: since we can have up to n open and n closed, if we've reached maxiumum of n open and n closed 
        IF open == n AND closed == n THEN # 
            ADD path TO results #save the combination
            RETURN 0 #stop exploring the path

        #Try adding an opening parenthesis if we haven't reached n yet
        IF open < n THEN #1st rule
            ADD "(" TO path #append a open parenthesis
            CALL backtrack(path, open + 1, closed) #recursive call, increment the open count, closed count remains same
            REMOVE last character FROM path #after recursion, we pop the character undo the choice to allow us to explore other combos
  #EX: for "((", path.pop() removes the last "(" so you can try adding ")" instead.
                              
       # Try adding a closing parenthesis as long its current count is less than the open count (same idea)
        IF closed < open THEN 
            ADD ")" TO path #append closing parethesis to our path
            CALL backtrack(path, open, closed + 1)  #recursive call, incrementing the closed count, open remains same
            REMOVE last character FROM path 


  #Start BACKTRACK with an empty path and 0 open and closed
    CALL backtrack("", 0, 0) #path is initially empty
    RETURN results #return list of valid parenthesis


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = [] #empty list that stores all valid combinations  

        #Helper function so we can 1)recursively call it, keep track of path and the counts
        def backtrack(path, open_count, close_count): 
          
          # Base case: if we used all open and closed parenthesis(limited up to n), save path to our result of all combos & stop exploring the path
            if open_count == n and close_count == n:
                res.append("".join(path))
                return 0

            # Add open parenthesis if we have used less than n pairs 
            if open_count < n:
                path.append("(")
                backtrack(path, open_count + 1, close_count) #recursive call, incremened open
                path.pop()  # after recursive backtracking, remove last parenthesis so can explored other valid combinations
                #EX: for "((", path.pop() removes the last "(" so you can try adding ")" instead.

            # Add closed parenthesis as long closed count is less than open 
            if close_count < open_count: #open must be greater bc must have the open must come before its closed to be a valid combo
                path.append(")")
                backtrack(path, open_count, close_count + 1) #increment closed
                path.pop()  # after backtracking, remove last parenthesis

        backtrack([], 0, 0) #call our function, start with a empty and 0 parenthesis
        return res #call completed functions

#Extra: I chose path not a stack : Path not a stack because we're  building a current solution/combination, 
#vs a stack trackes the nodes waiting to be explored(in a graph or tree)

  
