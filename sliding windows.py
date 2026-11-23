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
