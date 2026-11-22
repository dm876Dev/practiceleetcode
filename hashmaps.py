#hash maps insetion and lookup time are both O(1) constant time! TIME COMPLEXITY CONSTANT. 

#Two Sum lc 1
#https://github.com/neetcode-gh/leetcode/blob/main/python/0001-two-sum.py
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        count_index = {}  # will store each val and index, so we cna lookup later
        for i, num in enumerate(arr):#enuemrate gives index and element
          complement = target - num #complement the number we need to pair with the num to get target
          
          if complement in num_to_index: #checkour hash map if we've seen thsicomplement, if yes means sum of current numbers add up to target
            return [i, count_index[complement]] #so return its indices
          
          count_index[num]= i #if we havent seen it yet, we store the current number in the map with it's index, for later pairings
          return []

 #create a hashmap to store value and index 
 #find compliment whichis thethe number we need to pair with the num to get target
  #check if the current element exists in the hash map #it must be a differnent index, can tbe same element twice
  #if does exist, return the index and element of current complement  
  #if it doesnt, store the current number for later pairings(that reach the target)

          


#looping through entire array once, constant lookups and inserts so: T:O(N) 

