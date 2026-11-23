#Sliding windows

#Fixed window syntax:
def sliding_window_fixed (input, window_size): #Start by grabbing first window size element as our intial window
  ans = window = input[0:window_size]
  for right in range(window_size, len(input)): #loopfrom window size till end of input
    left = right - window_size #on each step we're caluclating left to give us idnex of element that just fell out of window 
    remove input[left] from window #remove old element from the window
    append input[right] to window #add new element right to the end
    ans = optimal(ans, window) #update our answer based on wtvr problem is asking(max,min,avg,etc)
  return ans




#easier-
#a is the input array we were given, iterable
#k is the fixed window size/sum (k elements)
#cur is a counter, the current window's sum or avg  
#best = largest sum across al windows so far


def sliding_window_fixed(a, k): #a = input array, k is window size
    cur = best = sum(a[:k]) #initialze the current sum and best answer with the calculated sum of the first k elements of array 
    for r in range(k, len(a)): #iterate over a range starting from the k(end point of the window) to the end of the array, keep looping
        cur = cur + a[r] - a[r-k] #add to the current sum the new right element and substract the left old element of the current window 
        best = max(best, cur) #min(), max() #update the best answer found so far with the largest between current window sum(counter) and best sum so far

    return best





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
