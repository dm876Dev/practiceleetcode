#https://leetcode.com/problems/valid-palindrome/
#opposite direction two pointer method
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s)-1
        while l < r:
            while l<r and not s[l].isalnum(): #checks if l pointer is not alphanumeric
                l+=1 #movingn it forward
            while l<r and not s[r].isalnum(): #checks if r pointer is not alphanumeric
                r-=1 #moving it backward 
            #now we have valid alphanumeric characters, we compare left and right chcarcters if different(ignoring the cases while doing so by converting them to lowercase)
            if s[l].lower() != s[r].lower(): #check if left and right characters are diff and concert them to lowercase
                return False #if last check don't work, exits the entire function
            #if checks pass, then skip if body and continue the loop 
            #move both pointers inwards -
            l += 1 
            r -= 1
        return True   #if entire loop passes all our checks, our string is a palidrome

    
#you can also do reversing the string with string slicing g [::-1]-

class Solution:
    def isPalindrome(self, s: str) -> bool:
        #use expression generator to create a new string
        
        # Create a new string using .join() on empty seperate '' to combine characters without spaces
        # and use generator expresion- new_list = [expression for item in iterable if condition]
        # it loops through each character in s, filters out anything that isn't a letter or number, 
        # and converts  remaining characters to lowercase, finally joins them together into new_string.
        
        new_string = ''.join(c.lower() for c in s if c.isalnum())
        
        if new_string != new.string[::-1]:
            return False
        return True

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Comparison check: Compare normal strings to reversed string, return False if they don't match
        if new_string != new_string[::-1]:
            return False

        # If they match, return True
        return True


class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_string = ''.join(c.lower() for c in s if c.isalnum())
        
        if new_string == new_string[::-1]:
            return True
        return False
#OR

        # if new_string != new_string[::-1]:
        #     return False
        # return True

    
#without using the built in  .isalnum() function you can create a helper function in the beginning

class Solution:
    def is_alphanumeric(c): #c is the input the function recieves
            return ('a' <= c.lower() <= 'z') or ('0' <= c <= '9') #any character fo the string between or include a-z and 0-9
            return ("a"<= c <= "z") or ("A"<= c <= 'Z') or ('0' <= c <= '9')

    def is_alphanumeric(c):
            return('a' <)
    def isPalindrome(self, s: str) -> bool:
        #Two pointer
        l, r= 0, len(s) -1
        while l < r :
            while l < r and not is_alphanumeric(s[l]): #if not alphanumeric skip over
                l += #traverse that string
            while l < r and not is_alphanumeric(s[r]):
                r -=
            if s[l].lower != s[r].lower:
                return False

            l += 1
            r -= 1

        return True
        #Reverse string usiing string slice method
        def is_alnum(c):
            return ('a'<= c <= 'z') or ('A'<= c <= 'Z') or ('0'<= c <= '9')
        
        def isPalindrome(self, s: str) -> bool:
            #generator expression, list comprehnesion type of msyntax
            #expression for c in iterable if condition
            new_string = ''.join(c.lower() for c in s if is_alnum(c))

            if new_string != new_string[::-1]:
                return False
            return True
            #return new_string == newstring[::-1]






#https://leetcode.com/problems/middle-of-the-linked-list/
#fast slow two pointer method(one direction):
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode | None) -> ListNode | None:
        slow = fast = head #same starting point

        while fast and fast.next: #while fast node and next node exists
            fast= fast.next.next #move the fast node forward by 2 nodes
            slow = slow.next #move forward by one node
        return slow #return the the middle one AKA second middle since this fucntion works for both examples even and odd num of nodes 

        #fast → True (a node exists)
        #fast.next → False (no next node exists)
        #while fast ndoe exists and next node after it exits, keep looping

class Solution:
    def middleNode(self, head: ListNode | None) -> ListNode | None:
        #fast and slow two pointer technique
        start = fast = head #set our two pointers to same starting vlaue
        while fast and fast.next: #while our first pointer to go eexists and the next ndoe also exists loop
            fast = fast.next.next #move node two nodes forward
            slow = slow.next #move mode one ndode foward
        return slow #same middle node as secodn middle ndoe value
        #fast is moving twice as fast as the slow so when it reachess the end slow pointer reaches the middle
        #second mdidle node means a linked list of even num of nodes has 2 middle nodes 3 and 4, so it woudl return 4 if it were even
        #Big O(n) tiem complexity bc its one loop through the structure


#https://leetcode.com/problems/palindrome-number/ 
class Solution:
    def isPalindrome(self, x: int) -> bool:
        #two pointer, more space-efficent O(1) constant extra space, compares without makign copy or even modifying:
        #T: O(1), S: O(1)
        s = str(x)
        l, r = 0, len(s)-1
        while l < r :
            if s[l] != s[r]: #can compare the characters from oppsoite ends without making a copy
                return False
            l += 1
            r -= 1
        return True
    # easy way, but less space efficent S: O(n), T: O(n)
    # creates new string in memroy takes up uncessary space
        s = str(x)
        return s == s[::-1]


#https://leetcode.com/problems/squares-of-a-sorted-array/
#two pointer way OPTIMIZED(AVOIDS REVERSING AT THE END!)-

#Because the sorted input guarantees the largest absolute value is at either end we can then use two pointers to acheivent mroe efficent time complexity: O(n) time.
#Since the input array is already sorted, the largest absolute value is guaranteed to be at one of the two ends.
#However, squaring can change their order, so we use two pointers to compare absolute values at both ends and place the largest square first,going inward filling new array from right to left.
# We're optimizing this way avoiding reversal step from  the other way which is building it largest to smallest then having to reverse it

class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
       #1 way
        l , r, i = 0, len(nums) -1, len(nums) -1 # tuple unpacking-of items need to match # of variables; CANT USE THE SAME VALUE for two diff variables ever.
        arr = nums.copy() #copy of array which we will overwrite later right to left, same length
        while l <= r:
            if abs(nums[l]) > abs(nums[r]): #if the left is BIGGER than right we move it up
                arr[i] = nums[l] **2
                l += 1
            else:
                arr[i]= nums[r] **2 #if the right pointer is SMALLER than right we move it back
                r -= 1
            i -= 1 # Move one position left in the arr
        return arr


#else insteadof another if statement bc its just convention rather than doign two ifs, also cus it checks the udpated values not original ones, and we wanna compare two original values each iteration!
#arr = [0] * len(nums) #  Preallocate an array filled with 0s as temporary placeholders(to allocate enough space), so we can fill it from right to left

#easy way
class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        #inuition is iterating through array squaring it, using sort built in function
       for i in range(len(nums)): #loop through index entire length not including last (0 to len(nums)-1, range ensures its ascending)
            nums[i] = nums[i] **2 
            #nums[i] **= 2 #square i: the current element times itself
       nums.sort()
       return nums

       #arr = sorted(nums) #nums.sort() #return True # Sorts in ascending order, modifying it
       #return arr
        #descending-
        #nums.sort(reverse = True return nums 
        #new_list =  sorted(nums, reverse = True) return new_list

       #Two pointer method(more efficent time complexity)- 
       #Two ways- 1) Building the result from smallest to largest and reversing
       #2) more optimized version- we fill the result array from the end(largest) to the beginning(progressively smaller inward)



            
        
