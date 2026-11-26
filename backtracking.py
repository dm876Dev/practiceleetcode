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
#
# Big idea
# Generate all valid combinations that produce ////
# adding one parenthesis at a time but only make a choice if it keeps the string valid. Backtrack to undo the choice 
#and try the other option.
#FIXXXXXXXXXXXXXX

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
      
      def dfs(path, open_count, close_count):
          #base case: reached a complete valid string when we've added 2*n parentheses
          if len(path) == 2 * n: 
              res.append("".join(path))  # join the path into a string and add it to results
              return
  
          #each step try adding either "(" or ")" to the current path
          for edge in ["(", ")"]:
  
              #prune early: skip choices that would make the parentheses invalid
              if edge == "(" and open_count == n:  # can't add more than n opening parentheses
                  continue
              if edge == ")" and close_count == open_count:  # can't close unless there's an unmatched "("
                  continue
  
              path.append(edge)  # add the chosen parenthesis to the current path

        dfs([], 0, 0)
        return res

1. Initialize: Create res to store completed valid strings.
2. Start DFS: Begin with an empty path and both open_count and close_count set to 0.
3. Base case: Once the path contains 2 * n parentheses, join it into a string, add it to res, and return.
4. Try choices: Loop through ( and ) as the next possible characters.
5. Prune early: Skip ( if we've already used n opening parentheses. Skip ) if there is no unmatched ( to close.
6. Add choice + update: Append the chosen parenthesis to path and update its corresponding count.
7. Recursive call: Call DFS to continue building the string with the updated path and counts.
8. Revert: Use path.pop() to remove the last choice so we can try another option.
9. Return: Once DFS finishes exploring all valid combinations, return res.
