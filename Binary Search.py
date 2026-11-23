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









    
