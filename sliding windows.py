#Sliding windows

#Fixed window syntax:

#a is the input array we were given, iterable
#k is the fixed window size/sum (k elements)
#cur is a counter, the current window's sum or avg  
#best = largest sum across al windows so far


def sliding_window_fixed(a, k): #a = input array, k = window size, number of consecutive k elements
    cur = best = sum(a[:k]) #initialze the current sum and best answer with the calculated sum of the first k elements of array 
    for r in range(k, len(a)): #iterate over a range starting from the k(end point of the window) to the end of the array, keep looping
        cur = cur + a[r] - a[r-k] #add to the current sum the new right element and substract the left old element of the current window 
        best = max(best, cur) #min(), max() #update the best answer found so far with the largest between current window sum(counter) and best sum so far

    return best

#643. Maximum Average Subarray I -SAME AS ABOVEE^^ - Fixed Size
class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        cur = best = sum(nums[:k])
        for r in range(k, len(nums)):
            cur += nums[r] - nums[r-k]
            best = max(cur, best)
        return (best / k)

#Syntax for Dynamic sized window:

#Longest subarray where sum of element is smaller than S(which is 15)-Dynamic 
l, curr, best = -1, 0, 0
for r in range(len(a)):
  curr += a[r]
  while curr >= S ##You must shrink the window until it becomes valid (curr < S). Then you record its length. 
    l+=1
    curr -= a[l]
  best = max(best, r-l) #do r-l because l starts before the start of array so like this gives accurate window length
#so best gives maximum window length (longest subarray) found so far
return best



#209: Minimum Size Subarray Sum -Dynamic  
class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        l, curr, best = 0, 0, len(nums) + 1 #large window length(more than possible) so first actual smallest window can replace it, not hard to find 
        for r in range (len(nums)):
            curr += nums[r]
            while curr >= target: #the window is already valid (curr >= target), you record its length, then shrink it to see if you can find an even shorter valid window.
                best = min(best, r - l + 1) #start with to find valid window length #add 1 bc l is the first index
                curr -= nums[l] #move left pointer inward
                l += 1
        return best if best != len(nums) + 1 else 0 #in problem!


      
class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        window = set() #initialize an empty set to track elements in the current window
        for r in range(len(a)): #iterate through the array using r as the right pointer
            if a[r] in window: #check if current element already exists in the window
                return True #return True if duplicate is found
            window.add(a[r]) #add the new right element to the window
            if r >= k: #check if the window has exceeded the allowed index distance
                window.remove(a[r-k]) #remove the old left element falling outside the allowed distance
        return False #return False if no nearby duplicates are found
            return False
      

def sliding_window_flexible_longest (input): #Start with empty window and grow it one element at a time from the right
  initialize window, ans
  left = 0
  for right in range (len (input)): #every time u add a new element check if widnow is still valid
    append input[rightl to window 
    while invalid(window): #if window is invalid, you start removing eelments fromt he left until becomes valid again
      remove input [left] from window
      left += 1
  ans = max(ans, window) #once window is valid update your answer trackkign the cahrarcters in widnow see if they meet condition
return ans 
