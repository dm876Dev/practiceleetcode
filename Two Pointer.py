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



#LeetCode 151 – Reverse Words in a String
#https://www.youtube.com/watch?v=-ggUxN7bFjU


# Logic: Parse out each word, store it in a list, then return the words in reverse order, joined with single spaces.
# One option(easy) is splitting the string into words, and reversing it afterward using built in reverse method
# Another easy cop out would be parse out the words, and append it to the end of a list, and reverse at the end
# My Strategy: Optimization in terms of time complexity: Use a double-ended queue (deque) & instead of appending each word to the end of our que
# we used appendleft to append to end of our deque, eliminate extra step


#1st solution- Split join Method:

class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()               # Split string into individual words (removes extra spaces)
        words.reverse()                 # Reverse the order of the words
        return " ".join(words)           # Join words with single spaces

T:O(N) S:O(N)

#2nd solution- String Builder Method
#Same direction two-pointer approach -to move (left to right) through the string
PSEUDOCODE
FUNCTION reverseWords(s):

    Create stringbuilder = deque()  # Storing our result, our words in reverse order
# double-ended que- a strcture that allows you you add/remove elements in constant time to both front/ back 

    start = 0 #initialize first pointer: starting index, beginning of word 
    i = 0 #second pointer: counter index, moves rightward to find end of the word

    WHILE i < length of s: #while we have not reached the end of the string
        IF s[i] is not a space: #find the start of a word
            start = i #save word's starting index

            WHILE i < length of s AND s[i] is not a space: #Continue until reaching a space(before it) or end of the string
                i += 1 #find the end of the word

            Add s[start:i] to LEFT of deque #next, we extract the word from starting index up to excluding index i
            #appendleft() we use to AVOID EXTRA STEP REVERSING AT THE END! bc it store in reverse order 
            #it adds to beginning of the deque: ["world", "hello"]
            #append() adds to the right (end of the deque): ["world", "hello"]
            #we must pair it with .reverse() at end which requires O(N) so more time  
        i += 1  #we can skip the space and move forward

    RETURNs our stringbuilder: the words joined with single spaces in between #" ".join(string_builder)

#TYPED CODE-
class Solution:
    def reverseWords(self, s: str) -> str:
        string_builder = collections.deque() #append to the left in constant time, so input will be in current order, and not need to reverse, saving one iteration
    #find all words in our string- identify start point continue right till hit white space, everything until that will be our word
    #in python, string slicing, the end is not inclusive so itll get the entire string there
        start = 0
        i = 0 #pointer
        while i < len(s): #while we havent reached end of string
            if s[i] != " ": #and is not at a space, we can store our start index
                start = i

                while i < len(s) and s[i] != " ": #parse out entire string; moving pointer forward until hit a space or the end
                    i += 1
                string_builder.appendleft(s[start: 1]) #extract the word from start up to, but not including, i
            i += 1  # move to the next character
        return " ".join(string.builder) #join the words with a single space between them and return the result
    
    #T: O(N) left to right thru string no going left to right thru string
    # S: O(N)  length of words in string, worst case in no white spaces bc we need to store every single word

#Recap (brief) or just read above-
# 1) Traverse the string from left to right and parse out each word.
# 2) Store each word in a deque using appendleft() to store in reverse order
# 3) Join the words using join method, empty string seperator, to separate them up w spaces
# 4) Return the final reversed string

#Difference in split vs dequue approaches
#split handles the parsing automatically, then reverse list VS deque you manually parse each word, use appendleft() 
#to build the reversed order immediately.

# Potential interview follow up-Can you solve this problem using less extra space, without a deque?
Yes. I can convert the string into a array using chars = list(s),  and modify in place which owuld give me O(1) space 
# which avoids creating a new array, or using a deque(which creates a new container).  I'd usechars.reverse() to 
#reverse entire string, and then  reverse again each individual word TO restore the Letter Order + clean 
#up the spacing. 

#344 Reverse String 

#1. Restate the problem
#"So we're given an array of characters, and we need to reverse the order of the characters by modifying the 
# original array."

#Should I treat letters and numbers the same way, or is there alphanumeric or special character rule i should account for?
#Im nodifying in place so it must modify the original array right are copies aren't allowed right?

#I'll use two pointers method: one pointer starts at the beginning of the array and one at the end. I'll swap 
#the characters at those positions, then them inward until they meet or cross. This reverses the array in-place 
#with O(1) extra space.
#Recursion is another option, but it requires O(n) call-stack space, so the iterative approach is more space-efficient.


#I'd also consider a few edge cases(from the examples): odd-length array like hello leaves the middle l character in place, 
#and an even-length array swaps every pair. also a single character requires no swaps.  So our code needs to accomodate that.

#1st solution- Two Pointers Method
class Solution:
    def reverseString(self, s: list[str]) -> None:
        # Time: O(n), Space: O(1)
        l = 0 #We're just storing those index positions in variables
        r = len(s)- 1 # two pointers, left will be index 0 , right is last index which is excluded so define as len(s) - 1
        while l < r : # stops when the two pointers meet or cross
            s[l], s[r] = s[r], s[l] #swap the two pointers, reassign two variables stimutaenously
            l += 1 #increment left point,
            r -= 1  #decrement right pointer
            #no return statement needed when you're modifying object in place.
    
# 1st Solution Logic: 
# Use two pointers: left starts at index 0, right at the last index.
# Swap the first and last characters, then move both pointers toward the center.
# Left pointer increments by 1; right pointer decrements by 1.
# Continue until the pointers meet or cross.
# The middle character (if odd length) stays in place.

#- Time: O(n)   Each swap handles 2 characters, so n characters require about n/2 operation so O(n/2) but drop constants → O(n).
#- Space: O(1)  Only two pointer variables (l and r); modify the original array in place.

#2nd Solution- Another way, that WOULD NOT achieve the constraint of O(1) extra space, but it would solve it is
#Recursion Method with a Helper Function 
    class Solution:
        def reverseString(self, s: list[str]) -> None:
            #Time : O(n), Space: O(n)
            def reverse(l,r): #reverse() is a helper function (function defined inside main function)
                if l<r: #base case, when l < r becomes false, the function stops
                    s[l], s[r] = s[r], s[l]
                    reverse(l + 1, r - 1) #calls the same helper function again, making it recursive
        reverse(0, len(s) - 1) #inital call to start the recursion

#2nd Solution Logic: w the recursion
# 1) Define a helper function reverse(l, r) that takes the left and right indexes.
# 2) Base case: Stop when l >= r (pointers meet or cross).
# 3) Swap s[l] and s[r].
# 4) Recursively call reverse(l + 1, r - 1) to move inward and reverse the remaining characters.
# 5) Start with reverse(0, len(s) - 1).

# The recursive solution is less space-efficient because each recursive call uses space on the call stack.
# Space: iterative is o(1) vs recursive is O(n)


