#Syntax

#Standard Dinary Search- Find an exact target value in a sorted array.
def binary_search(arr: list, target: int) -> int: #Vanilla BSS Syntax (looking for target number in  a sorted array)
    left, right = 0, len(arr)-1
    while left <= right:
      mid = (lef + right)/2
      if arr[mid] == target:
        return mid
      elif arr[mid] < target:
        left = mid + 1
      else:
        right = mid - 1
    return -1

#With intuitive commaents
def binary_search(arr: list, target: int):
    left, right = 0, len(arr) - 1 # initialize left and right pointers at the ends of the array

    while left <= right: #while they havent crossed (= include)
        mid = (left + right) // 2 # find the middle index (left + rigght)/2
        if arr[mid] == target: # check if the middle element (its INDEX) is the target 
            return mid # return mid -we found our target!
        elif arr[mid] < target: # if middle element is smaller than target
            left = mid + 1 # search the right half -> shift left to 1 past mid (mid+1)
        else: # if middle element is larger than target
            right = mid - 1 # search the left half -> shift right to 1 prior mid (mid-1)

    return -1 # return -1 if target is nto in the array!

# Binary Search on a Monotonic Condition (First True Binary Search)
# The condition changes in only one direction, like a linear sequence.
# Example: [False, False, False, True, True, True]
# Binary search finds the first True: everything before it is False, and everything after it is True.

## We're looking for the first True, not just any True, so we keep searching earlier : 2 exs:  first_true_index = -1; if no True is found, return -1.

def binary_search(arr: List[int], target: int):
    left, right = 0, len(arr) - 1
    first_true_index = -1 # store best candidate so far; keep searching earlier, hence -1
    while left <= right:
        mid = (left + right) // 2 # find middle index
        if feasible(mid): # check if mid satisfies the condition (returns True or False)
            first_true_index = mid # if valid, store it as the best candidate so far
            right = mid - 1 # keep exploring earlier indexes to find the first True
        else:
            left = mid + 1 # if not feasible, search the right half
            
    return first_true_index # return first True index, or -1 if no valid candidate was found


#LEETCODES PROBLEMS from past 3 months should prioritize these

# First priority- ast 30 days, then rest
# 1. Binary Search (Easy)
# 2. oko Eating Bananas (Medium)
# 3. Search Insert Position (Easy)
# 4. Find First and Last Position of Element in Sorted Array (Medium)
# 5. Search in Rotated Sorted Array (Medium)
# 6. Find Minimum in Rotated Sorted Array (Medium)

# Last priority
# 6. Valid Perfect Square (Easy)
# 7. Sqrt(x) (Easy)
# 8. Find Peak Element (Medium)
# 9. Single Element in a Sorted Array (Medium)

#4 Types you need to practice-
# 1. Classic Binary Search LEARNED
# - Find a target in a sorted array.
# - Compare arr[mid] with target.
# - Eliminate half the search space each time.
# Practice:
# - Binary Search
# - Search Insert Position

# 2. Boundary Binary Search (First / Last Occurrence)
# - Find the first or last position where a condition is true.
# - Instead of stopping when you find a match, keep searching for an earlier or later match.
# - Often uses answer = -1 to store the best candidate.
# Practice:
# - Find First and Last Position of Element in Sorted Array

# 3. Modified Binary Search (Rotated / Partially Sorted Arrays)
# - The array is sorted but has been rotated or changed in some way.
# - Figure out which half is still sorted, then decide where to search.
# Practice:
# - Search in Rotated Sorted Array
# - Find Minimum in Rotated Sorted Array

# 4. Binary Search on the Answer (Feasibility / First True) LEARNED
# - You're not searching for a target in an array.
# - You're searching for the smallest or largest possible answer.
# - Use a feasible(mid) function to check whether a candidate answer works.
# - Narrow the search based on True/False.
# Practice:
# - Koko Eating Bananas
# - Minimum Size Subarray Sum (also sliding window)



    
