#https://leetcode.com/problems/valid-palindrome/
#opposite direction two pointer method
class Solution:
    def validPalindrome(self, s: str) -> bool:
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
    def validPalindrome(self, s: str) -> bool:
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
    def validPalindrome(self, s: str) -> bool:
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
    def PalindromeNumber(self, x: int) -> bool:
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

#2. Clarifying questions
#Should I treat letters and numbers the same way, or is there alphanumeric or special character rule i should account for?
#Im nodifying in place so it must modify the original array right are copies aren't allowed right?

#3 Strategy/method, trade offs
#I'll use two pointers method: one pointer starts at the beginning of the array and one at the end. I'll swap 
#the characters at those positions, then them inward until they meet or cross. This reverses the array in-place 
#with O(1) extra space.
#Recursion is another option, but it requires O(n) call-stack space, so the iterative approach is more space-efficient.

#4. Edge cases
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


# =============================================================================
#283 Move Zeroes
# =============================================================================

#1. Restate the problem
#"So basically I've got a list of numbers, and I need to push every zero to the back while the other numbers
# keep the order they were already in. And I have to do it right on that same list, not by building a new one."

#2. Clarifying questions
#Can I assume the array can be empty or have one element? 
#Are there constraints on extra space, or must it be O(1)? Im assuming no copying the array.

#3. Strategy/method, trade offs
#I'll use two pointers (same direction, slow and fast). Fast scans every element; slow marks where the next
#non-zero goes. When fast finds a non-zero, swap it into slow's spot and move slow forward. O(n) time, O(1) space.
#A new list would work too, but costs O(n) extra space.

#4. Edge cases
#All zeros [0,0,0] -> nothing changes. No zeros [1,2,3] -> swaps happen with itself, still fine.
#Single element -> nothing to do.

#1st solution- Two Pointers Method
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        # Time: O(n), Space: O(1)
        slow = 0 #slow pointer: where the next non-zero should go
        for fast in range(len(nums)): #fast pointer: scans every element once
            if nums[fast] != 0: #found a non-zero
                nums[slow], nums[fast] = nums[fast], nums[slow] #swap it into the slow spot (if slow == fast it swaps w/ itself, harmless)
                slow += 1 #next non-zero goes one spot to the right
        #no return statement needed, we modify nums in place

# 1st Solution Logic:
# Everything LEFT of slow is already the non-zero elements in their original order.
# Everything between slow and fast is zeros (they got skipped over).
# Each time fast finds a non-zero, swapping puts it at slow and pushes a zero toward the right.

#- Time: O(n)  fast visits each element once.
#- Space: O(1) only two index variables.


# =============================================================================
#27 Remove Element
# =============================================================================

#1. Restate the problem + claryfying question
"Just to make sure I understand, I'm given an integer array and a target number, and I need to clear out every copy of that number by moving the
# leftover numbers to the front of the list. Then I give back how many numbers I kept. I don't need to worry about anything beyond that count. Is that correct?"


#3. Strategy/method, trade offs
#Two pointers method (slow and fast). Fast scans every element; slow only moves when fast finds a non-val, and we
#overwrite at slow. Final slow = k. Overwriting is enough since we don't need to keep val. O(n) time, O(1) space.


#4. Edge cases
#Empty array -> return 0. Every element equals val [3,3,3], val = 3 -> return 0, slow never moves.
#No element equals val [1,2,3], val = 4 -> every element gets copied onto itself, return len(nums).
#Single element -> return 0 if it equals val, otherwise 1.

#1st solution- Two Pointers Method
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Time: O(n), Space: O(1)
        slow = 0 #slow pointer: next slot for a keeper, also becomes the count k
        for fast in range(len(nums)): #fast pointer: scans every element once
            if nums[fast] != val: #found a keeper (not val)
                nums[slow] = nums[fast] #overwrite the slow spot with it (if slow == fast it copies onto itself, harmless)
                slow += 1 #next keeper goes one spot to the right
        return slow #unlike Move Zeroes we DO return: slow = k, the number of elements that are not val

# 1st Solution Logic:
# Everything LEFT of slow is already the keepers (non-val), packed at the front in their original order.
# Everything between slow and fast is leftover values we don't care about (skipped vals or already-copied keepers).
# Each time fast finds a non-val, it gets copied to slow's spot. Elements equal to val are just skipped,
# so they get overwritten later or end up past index k, where we don't care.
# When fast reaches the end, slow = k.

#- Time: O(n)  fast visits each element once.
#- Space: O(1) only two index variables, nums is modified in place.


# =============================================================================
#88 Merge Sorted Array
# =============================================================================

#1. Restate the problem
#"So we're given two sorted arrays, nums1 with m elements followed by n empty slots and nums2 with n elements,
# and we need to merge nums2 into nums1 so that nums1 ends up as one sorted array, in place."

#2. Clarifying questions
#Is extra space allowed, or does this have to be O(1)? (That decides between copying nums1 and filling from the back.)
#Since 0 can be a real value too, can I rely on m and n to know where nums1's real data ends, instead of the zeros?

#3. Strategy/method, trade offs
#Merging from the front would overwrite nums1 values I still need, so I'll fill from the BACK with three pointers:
#i on nums1's last real element, j on nums2's last, k on nums1's last slot. Place the bigger of the two at k
#each time and move that pointer (and k) left. O(m + n) time, O(1) space.
#Another option is to copy nums1's real elements into a new list and merge from the front, but that costs O(m) space.
#Append nums2 and sort also works, but it's O((m + n) log(m + n)) and ignores that both are already sorted.

#4. Edge cases
#n == 0 (nums2 empty) -> the loop never runs, nums1 is already the answer.
#m == 0 (nums1 has no real elements) -> i = -1, so the i >= 0 check fails every time and nums2 gets copied in.
#All of nums2 is bigger [1,2,3,0,0,0] + [4,5,6] -> nums2 fills the back, nums1's elements never move.
#All of nums2 is smaller [4,5,6,0,0,0] + [1,2,3] -> nums1's elements shift right first, then nums2 fills the front.
#Equal values -> the else branch takes nums2's value, which is fine since equal values are interchangeable.

#PSEUDOCODE
#FUNCTION merge(nums1, m, nums2, n):
#
#    i = m - 1  #pointer at last real element of nums1
#    j = n - 1  #pointer at last element of nums2
#    k = m + n - 1  #pointer at the last slot of nums1, where the biggest remaining value goes
#
#  while j still has elements:   #while nums2 still has elements, loops, the rest of nums1 is already in place
#    if i still has elements and nums1[i] > nums2[j]:  #nums1's element is bigger
#        nums1[k] = nums1[i], i -=1
#    else:  #nums2's element is bigger/equal, or nums1 ran out
#        nums1[k] = nums2[j], j -=1
#   k-=1  #that slot is filled
#
#  no return, nums1 is modified in place



#1st solution- Three Pointers Method (filling from the back)
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # Time: O(m + n), Space: O(1)
        i = m - 1 #pointer at the last REAL element in nums1 (skips the empty slots)
        j = n - 1 #pointer at the last element in nums2
        k = m + n - 1 #pointer at the last slot in nums1, where the largest remaining value goes

        while j >= 0: #stop when nums2 is used up; leftover nums1 elements are already in the right place
            if i >= 0 and nums1[i] > nums2[j]: #nums1 still has elements AND its element is bigger
                nums1[k] = nums1[i] #place nums1's element at the back
                i -= 1 #nums1's pointer moves left
            else: #nums2's is bigger/equal OR nums1 has no elements left (i < 0)
                nums1[k] = nums2[j] #place nums2's element at the back
                j -= 1 #nums2's pointer moves left
            k -= 1 #slot k is filled either way, move left
        #no return statement needed, we modify nums1 in place

# 1st Solution Logic:
# Everything to the RIGHT of k is already the largest values in sorted order (final position).
# Filling from the back means we never overwrite a nums1 element we still need, because k = i + j + 1,
# so k stays ahead of i for as long as nums2 has elements left.
# We only loop while j >= 0: once nums2 is used up, the remaining nums1 elements are already in place.
# Tracing nums1 = [1,2,3,0,0,0], nums2 = [2,5,6]: 6 goes to the back, then 5, then nums1's 3, then nums2's 2,
# and the leftover 1,2 in nums1 are already correct -> [1,2,2,3,5,6].

#- Time: O(m + n)  each step moves one pointer left, and each element is placed exactly once.
#- Space: O(1)  merging happens inside nums1, only three index variables.


# =============================================================================
#21 Merge Two Sorted Lists
# =============================================================================

#1. Restate the problem
#"So we're given the heads of two sorted linked lists, and we need to merge them into one sorted linked list
# by splicing their nodes together, and return the head of the merged list."

#2. Clarifying questions
#When both lists have an equal value, does it matter which node comes first (stable merge), or are they interchangeable?
#Is recursion fine, or do you prefer iterative so there's no call-stack space?

#3. Strategy/method, trade offs
#Two pointers, one per list, plus a DUMMY node so the head isn't a special case. A tail pointer builds the result:
#attach the smaller current node and advance that list. When one runs out, attach the rest of the other.
#O(n + m) time, O(1) space. Recursion works too but uses O(n + m) call-stack.

#4. Edge cases
#Both empty -> return None. One empty -> return the other list. Equal values -> either one first is fine.

#PSEUDOCODE
#
#FUNCTION mergeTwoLists(list1, list2):
#    dummy = new node  #placeholder so the first real node isn't a special case
#    tail = dummy  #tail always points at the last node of the merged list
#
#    while list1 and list2:  #while both lists have nodes, loops
#        if list1.val <= list2.val:  #list1's node is smaller
#            tail.next = list1, list1 forward  #attach the smaller node, move that list forward list = list.next
#        else:  #list2's node is smaller
#            tail.next = list2, list2 forward  #attach the smaller node, move that list forward
#        tail forward #move tail onto the node we just attached
#
#    tail.next = whichever list has nodes left  #at most one does, it's already sorted so attach it whole
#
#    return dummy.next  #skip the dummy placeholder



class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Time: O(n + m), Space: O(1)
        dummy = ListNode() #placeholder node, its .next will be the real head
        tail = dummy #tail = last node of the merged list so far

        while list1 and list2: #both lists still have nodes
            if list1.val <= list2.val:
                tail.next = list1 #attach the smaller node
                list1 = list1.next #advance that list
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next #move tail forward to the node we just added

        tail.next = list1 or list2 #attach whichever list still has nodes (the other is None)
        return dummy.next #real head is right after the dummy

# Solution Logic:
# The dummy node removes the "is the result empty yet?" check.
# Each step we pick the smaller current node, so the merged list stays sorted.
# Leftover nodes are already sorted, so we attach them in one step.

#- Time: O(n + m)  each node is visited once.
#- Space: O(1)  we reuse the existing nodes, only dummy + tail are extra.


# =============================================================================
#1768 Merge Strings Alternately
# =============================================================================

#1. Restate the problem
#"So we're given two strings, word1 and word2, and we need to merge them by adding letters in alternating order,
# starting with word1. If one string is longer, we add its extra letters to the end, then return the merged string."

#2. Clarifying questions
#Is it okay to use built-ins like zip_longest, or do you want the pointers written out by hand?
#Can I assume both inputs are valid strings, or should I handle None?

#3. Strategy/method, trade offs
#Two pointers, i on word1 and j on word2. While both have letters, add word1[i] then word2[j] and move both.
#Then append the leftover of the longer word with a slice. O(n + m) time and space.
#I build a list and join at the end, which beats repeated string concatenation (+=) since strings are immutable.
#Another option is one loop up to max(len) with bounds checks on each word, or itertools.zip_longest,
#but the two-pointer loop + slice avoids checking the bounds on every step.

#4. Edge cases
#Same length "abc", "pqr" -> "apbqcr" (pure alternation, both slices at the end are empty).
#word1 shorter "ab", "pqrs" -> "apbq" + leftover "rs" -> "apbqrs".
#word2 shorter "abcd", "pq" -> "apbq" + leftover "cd" -> "apbqcd".
#One empty "", "xyz" -> the loop never runs, the slices add all of "xyz". Both empty -> "".

#PSEUDOCODE
#FUNCTION mergeAlternately(word1, word2):
#
#    result = []  #list of characters/pieces, joined at the end
#    i = 0  #pointer for word1
#    j = 0  #pointer for word2
#
#    WHILE i < length of word1 AND j < length of word2:  #both still have letters
#        Add word1[i] to result
#        Add word2[j] to result
#        i += 1
#        j += 1
#
#    Add word1[i:] to result  #leftover of word1 (empty string if none)
#    Add word2[j:] to result  #leftover of word2 (empty string if none)
#
#    RETURN result joined into one string

#1st solution- Two Pointers Method (one pointer per word)
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # Time: O(n + m), Space: O(n + m)
        res = [] #list of characters/pieces, joined at the end (faster than += on a string)
        i = j = 0 #i = pointer for word1, j = pointer for word2, both start at the front

        while i < len(word1) and j < len(word2): #while both words still have letters, loops
            res.append(word1[i]) #word1 goes first
            i += 1 #move word1's pointer forward
            res.append(word2[j]) #then word2
            j += 1 #move word2's pointer forward

        res.append(word1[i:]) #leftover of word1, empty string if it was used up
        res.append(word2[j:]) #leftover of word2, only one of these two has anything

        return "".join(res) #glue all the pieces into the final string


# 1st Solution Logic:
# The while loop handles the alternating part and stops as soon as the SHORTER word runs out.
# At that point one pointer is at the end of its word, so its slice is "" (adds nothing),
# and the other slice grabs the entire leftover of the longer word in one step.
# Tracing "ab", "pqrs": a, p, b, q -> loop ends (i = 2) -> word1[2:] = "" and word2[2:] = "rs" -> "apbqrs".

#- Time: O(n + m)  every character is visited or sliced once, and join is linear.
#- Space: O(n + m)  the output string holds all characters (the list of pieces is the same size).



=============================================================================
#28 Find the Index of the First Occurrence in a String
# =============================================================================

#1. Restate the problem
#"So we're given two strings, haystack and needle, and I need to return the index where needle first shows up
# inside haystack, or -1 if it never appears."

#2. Clarifying questions
#Are built-ins like haystack.find(needle) or slicing allowed, or do you want the matching written out by hand?
#Should I expect big inputs where an O(n * m) approach could be too slow, or is a simple approach fine to start with?
#Should I trust the input types, or defensively handle None?

#3. Strategy/method, trade offs
#Sliding window: i marks where a window starts in haystack, and the window is as long as needle.
#Compare the window to needle at each i. The last valid start is len(haystack) - len(needle), so I stop there.
#O(n * m) time. It's simple and fast in practice, but slicing makes a temporary copy of size m, so a manual char-by-char compare would be O(1) space.
#KMP guarantees O(n + m) even on adversarial inputs like "aaaa...ab", but it costs an extra table and much trickier code,
#so I'd start simple and only upgrade to KMP if the inputs are large or they ask for linear time.

#4. Edge cases
#needle longer than haystack -> range is empty, return -1.
#needle == haystack -> match at index 0.
#Match at the very end "sadbutsad", "sad" -> i = 6 must be included in the range, so +1 on the bound.
#Partial matches that fail "aaab", "aab" -> window "aaa" fails, window "aab" at i = 1 matches.

#1st solution- Sliding Window (compare slices)
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Time: O(n * m), Space: O(m) for the slice (O(1) if compared char by char)
        n, m = len(haystack), len(needle) #store lengths so we don't recompute them
        for i in range(n - m + 1): #i = window start, last valid start is n - m, +1 because range excludes the end
            if haystack[i:i + m] == needle: #window of length m equals needle
                return i #first match, so return immediately
        return -1 #never matched

# 1st Solution Logic:
# Every possible starting index is checked left to right, so the first match we hit is the earliest one.
# If needle is longer than haystack, n - m + 1 <= 0, the loop never runs and we fall through to -1.
# Tracing "hello", "ll": n = 5, m = 2 -> i = 0 "he", i = 1 "el", i = 2 "ll" -> return 2.

#- Time: O(n * m)  up to n - m + 1 windows, each compare costs up to m.
#- Space: O(m)  the slice is a temporary copy; no other extra structures.


#2nd solution- In case slicing isn't allowed: compare char by char with an inner pointer (same time, true O(1) space)
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Time: O(n * m), Space: O(1)
        n, m = len(haystack), len(needle)
        for i in range(n - m + 1): #i = window start in haystack
            j = 0 #j = pointer inside needle
            while j < m and haystack[i + j] == needle[j]: #keep going while the characters match
                j += 1 #both pointers move forward together (i + j in haystack, j in needle)
            if j == m: #j walked all the way through needle, so the whole needle matched
                return i
        return -1

# 2nd Solution Logic:
# Same idea as the 1st, but instead of making a slice we compare one character at a time and stop at the first mismatch.
# That avoids the O(m) temporary copy, and on mismatches it usually bails out early.
# Worst case is still O(n * m), e.g. haystack "aaaaaa", needle "aaab".
# (One-liner if built-ins are allowed: return haystack.find(needle))

#- Time: O(n * m)  worst case, every window matches almost all the way.
#- Space: O(1)  only i and j.


=============================================================================
#16 3Sum Closest
# =============================================================================

#1. Restate the problem
#"So we're given an integer array and a target, and we need to find three numbers whose sum is as close to the
# target as possible, and return that sum, not the numbers themselves."

#2. Clarifying questions
#Is it okay to sort nums in place, or should the caller's array stay untouched? (Leaving it alone costs an O(n) copy.)
#Roughly how large can the array get? That decides whether O(n^2) is needed or O(n^3) brute force is fine.
#Do the three numbers have to come from three different positions, even if the values repeat?

#3. Strategy/method, trade offs
#Sort first, then fix one number with i and use two pointers l and r on the rest of the array.
#If the sum is below target I need it bigger, so l moves right. If above, r moves left. Track the sum with the
#smallest distance to target. If the sum equals target exactly, return early since the distance can't be smaller.
#O(n^2) time. Brute force with three nested loops is O(n^3) but needs no sorting and is the easiest to get right,
#so it's a fine baseline for small inputs; sorting costs O(n log n) up front and reorders the caller's array,
#but that's a small price since the two-pointer pass is what drops the time from cubic to quadratic.

#4. Edge cases
#Exactly 3 numbers -> the only possible sum is the answer.
#Exact match exists -> return the target immediately.
#All negatives or all positives -> still works, sorting + pointers don't depend on signs.
#Duplicates -> don't affect correctness here, since we only need the closest sum, not unique triplets.

#Pseudo code:
#FUNCTION threeSumClosest(nums, target)
#
#    SORT nums #sorted order is what tells the pointers which direction to move
#    closest = nums[0] + nums[1] + nums[2] #starting guess, any real triplet sum works so we have something to compare against
#
#    # Fix one number at a time, then squeeze two pointers on the rest of the array
#    FOR i FROM 0 TO length of nums - 3 DO #i = the fixed number, leave room for l and r after it
#        l = i + 1 #left pointer starts right after i
#        r = length of nums - 1 #right pointer starts at the last index
#
#        WHILE l < r DO #stop when the pointers meet
#            total = nums[i] + nums[l] + nums[r] #current triplet sum
#
#            # Exact hit: the distance can't get smaller than 0, so we're done
#            IF total == target THEN
#                RETURN total #return the exact match
#
#            # Is this sum closer to target than the best one so far?
#            IF ABS(total - target) < ABS(closest - target) THEN
#                closest = total #save it as the new best
#
#            # Move a pointer so the next sum lands closer to target
#            IF total < target THEN #sum is too small
#                l = l + 1 #move left pointer right to get a bigger number
#            ELSE #sum is too big
#                r = r - 1 #move right pointer left to get a smaller number
#  #EX: sorted [-4,-1,1,2], target 1: i = 0 gives -4 + -1 + 2 = -3 then -4 + 1 + 2 = -1, i = 1 gives -1 + 1 + 2 = 2 (distance 1) -> closest = 2
#
#    RETURN closest #best sum seen across all the triplets we checked

#1st solution- Sort + Two Pointers
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # Time: O(n^2), Space: O(1) extra (O(n) or O(log n) depending on the sort)
        nums.sort() #sorted order is what lets pointers decide which direction to move
        closest = nums[0] + nums[1] + nums[2] #starting guess, any real triplet sum works

        for i in range(len(nums) - 2): #i = fixed number, leave room for l and r after it
            l, r = i + 1, len(nums) - 1 #two pointers on the rest of the array

            while l < r: #pointers haven't met yet
                total = nums[i] + nums[l] + nums[r] #current triplet sum

                if total == target: #exact hit, can't do better
                    return total

                if abs(total - target) < abs(closest - target): #this sum is closer than the best so far
                    closest = total #update the best

                if total < target: #sum too small
                    l += 1 #bigger number on the left
                else: #sum too big
                    r -= 1 #smaller number on the right

        return closest #best sum seen across all triplets we checked

# 1st Solution Logic:
# Sorting means that moving l right can only increase the sum and moving r left can only decrease it.
# So for each fixed i, the pointers walk toward the target instead of trying every pair.
# We never need to compare unique triplets, only distances, so no duplicate skipping is needed.
# Tracing [-1,2,1,-4], target 1: sorted [-4,-1,1,2]. i = 0: -4 + -1 + 2 = -3, then -4 + 1 + 2 = -1.
# i = 1: -1 + 1 + 2 = 2 -> distance 1, closest = 2.

#- Time: O(n^2)  sort is O(n log n), then n iterations of i, each with an O(n) two-pointer pass.
#- Space: O(1)  only a few variables beyond the sort.


#2nd solution- Brute Force (three nested loops), the fallback if they want to see the baseline first
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # Time: O(n^3), Space: O(1)
        closest = nums[0] + nums[1] + nums[2] #starting guess
        for i in range(len(nums) - 2): #first number
            for j in range(i + 1, len(nums) - 1): #second number, always after i
                for k in range(j + 1, len(nums)): #third number, always after j
                    total = nums[i] + nums[j] + nums[k]
                    if abs(total - target) < abs(closest - target): #closer than the best so far
                        closest = total
        return closest

# 2nd Solution Logic:
# Try every possible set of three different indexes and keep the sum closest to target.
# Correct and simple, but too slow for large inputs, which is why sorting + two pointers is the better answer.
# Starting j after i and k after j means each triplet is checked once.

#- Time: O(n^3)  three nested loops over the array.
#- Space: O(1)  no sorting, only the closest variable.

=============================================================================
#15 3Sum
# =============================================================================

#1. Restate the problem
#"So we're given an integer array, and we need to return all the unique triplets that add up to zero.
# The triplets can't repeat, even if the same values show up at different indexes."

#2. Clarifying questions
#Is it okay to sort the array in place, since we return values and not indexes?
#Is extra space allowed (like a hash set), or should I aim for O(1) extra space?
#If the array has a lot of repeated values, should I worry about performance there, or is it enough that the output has no repeated triplets?

#3. Strategy/method, trade offs
#Sort, then fix one number with i and use two pointers l and r to find pairs that sum to -nums[i].
#Sorting also puts duplicates next to each other so they're easy to skip: skip a repeated i, and after a
#match skip repeated values for l. O(n^2) time and O(1) extra space, and the sort is just O(n log n) on top, so it never dominates.
#A hash set per i also gets O(n^2) time without the pointers, but it needs O(n) extra space and the duplicate handling is messier.
#Brute force with three loops is O(n^3) and would need a set of tuples to remove repeats, so it's the worst on both time and space.

#4. Edge cases
#Fewer than 3 elements -> loop never runs, return [].
#All zeros [0,0,0,0] -> exactly one triplet [0,0,0], not four, so duplicate skipping matters.
#nums[i] > 0 -> sorted, so every number after it is positive too, no triplet can sum to 0, we can break early.
#No valid triplet [1,2,3] -> return [].

#1st solution- Sort + Two Pointers
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Time: O(n^2), Space: O(1) extra, not counting the output (O(n) or O(log n) for the sort)
        nums.sort() #sorting lets us use pointers and puts duplicates side by side
        res = [] #all unique triplets go here

        for i in range(len(nums) - 2): #i = fixed number, need two more after it
            if nums[i] > 0: #smallest number is positive, so the sum can never be 0
                break
            if i > 0 and nums[i] == nums[i - 1]: #same fixed value as the previous i, skip to avoid duplicate triplets
                continue

            l, r = i + 1, len(nums) - 1 #two pointers on the rest of the array
            while l < r: #pointers haven't met yet
                total = nums[i] + nums[l] + nums[r]

                if total < 0: #too small
                    l += 1 #bigger value on the left
                elif total > 0: #too big
                    r -= 1 #smaller value on the right
                else: #total == 0, found one
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1 #move both inward to look for the next pair
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]: #skip repeated left values so we don't re-add the same triplet
                        l += 1

        return res

# 1st Solution Logic:
# Fixing i turns the problem into Two Sum on a sorted array: find l, r with nums[l] + nums[r] == -nums[i].
# Duplicate control happens in two places: skipping a repeated i, and skipping a repeated l after a match.
# We only need to skip l after a match; r takes care of itself, because once l moves to a new value
# the sum changes and r adjusts on the next iterations.
# Tracing [-1,0,1,2,-1,-4] -> sorted [-4,-1,-1,0,1,2].
# i = 1 (-1): l = 2 (-1), r = 5 (2) -> sum 0 -> add [-1,-1,2]. Then l = 3 (0), r = 4 (1) -> add [-1,0,1].
# i = 2 is also -1, equals nums[1] -> skipped. Result [[-1,-1,2],[-1,0,1]].

#- Time: O(n^2)  sort is O(n log n), then each i runs one O(n) two-pointer pass.
#- Space: O(1)  extra variables only, the output list isn't counted.

# =============================================================================
#11 Container With Most Water
# =============================================================================

#1. Restate the problem
#"So we're given an array of heights, each one is a vertical line. We need to pick two lines that, together with
# the x-axis, hold the most water, and return that max amount."

#2. Clarifying questions
#Do I only need the max area, or also which two lines produce it?
#If several pairs tie for the max area, does it matter which one I find? (Only matters if the pair is needed.)
#Should I treat the input as read-only? (The two pointers approach never changes it anyway.)

#3. Strategy/method, trade offs
#Two pointers from both ends. Area = min(height[l], height[r]) * (r - l). Then move the pointer at the SHORTER line inward:
#the width is shrinking, so the only way to beat the current area is to find a taller shorter-side.
#Moving the taller line can never help because the shorter line still caps the height. O(n) time, O(1) space.
#Brute force checking every pair is O(n^2), which is simpler to write and obviously correct, but it's too slow for big inputs
#and the two pointer version gives the same answer by safely skipping pairs that can't win.

#4. Edge cases
#Two lines only [1,1] -> one container, area 1.
#All heights equal -> the widest pair wins, so the first area computed is already the max.
#A height of 0 on one side -> area 0, move that pointer and keep going.
#Strictly increasing or decreasing heights -> pointers still converge in n - 1 steps.

#1st solution- Two Pointers Method
class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Time: O(n), Space: O(1)
        l, r = 0, len(height) - 1 #start with the widest possible container
        best = 0 #max area seen so far

        while l < r: #stops when the pointers meet, since a container needs two different lines
            area = min(height[l], height[r]) * (r - l) #shorter line sets the height, index gap is the width
            best = max(best, area) #keep the bigger one

            if height[l] < height[r]: #left line is shorter
                l += 1 #move the shorter side, it's the one limiting the area
            else: #right is shorter or equal
                r -= 1

        return best

# 1st Solution Logic:
# Start at max width. Every step the width shrinks by 1, so the area can only improve if the limiting height goes up.
# The limiting line is the shorter one, so that's the pointer we throw away.
# Moving the taller pointer would leave the same (or smaller) cap with less width, so it can never be better.
# Tracing [1,8,6,2,5,4,8,3,7]: l = 0, r = 8 -> min(1,7) * 8 = 8, move l. l = 1, r = 8 -> min(8,7) * 7 = 49 -> best.
# Nothing after that beats 49.

#- Time: O(n)  each step moves one pointer inward, so at most n - 1 steps.
#- Space: O(1)  only l, r, area and best.


#2nd solution- Brute Force (check every pair), the fallback baseline
class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Time: O(n^2), Space: O(1)
        best = 0
        for i in range(len(height)): #left line
            for j in range(i + 1, len(height)): #right line, always after i
                area = min(height[i], height[j]) * (j - i) #shorter line sets the height, index gap is the width
                best = max(best, area)
        return best

# 2nd Solution Logic:
# Try every pair of lines and keep the biggest area. Obviously correct, but too slow for n up to 10^5.
# The two pointer solution gets the same answer because it safely skips pairs that can't beat the current best.

#- Time: O(n^2)  every pair of lines is checked.
#- Space: O(1)  only best and area.


# =============================================================================
#75 Sort Colors
# =============================================================================

#1. Restate the problem
#"So we're given an array with only 0s, 1s and 2s, representing red, white and blue, and I need to sort it in place
# so all 0s come first, then 1s, then 2s, without using a library sort function."

#2. Clarifying questions
#Is a one-pass solution required, or is a two-pass counting solution acceptable?
#Does O(1) extra space have to be strict, or is a small fixed-size count array fine?
#Should I defensively handle values outside 0, 1, 2, or can I trust the input?

#3. Strategy/method, trade offs
#Three pointers (Dutch National Flag), one pass. l = where the next 0 goes, r = where the next 2 goes, i = scanner.
#If nums[i] is 0, swap with l and move both l and i. If it's 2, swap with r and move only r.
#If it's 1, just move i. O(n) time, O(1) space.
#Counting sort (count the 0s, 1s, 2s, then overwrite) is also O(n) time and O(1) space and much easier to get right,
#but it takes two passes; the Dutch flag does everything in one pass but the pointer rules are easy to mess up,
#especially not moving i after swapping with r.

#4. Edge cases
#Single element -> nothing to do.
#Already sorted [0,1,2] -> every swap is with itself or skipped, fine.
#All the same value [2,2,2] -> every element swaps with r until i passes r.
#Reverse order [2,1,0] -> 2 goes to the back, then the 0 gets pulled to the front.

#1st solution- Three Pointers (Dutch National Flag)
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        # Time: O(n), Space: O(1)
        l = 0 #boundary: everything LEFT of l is a 0
        r = len(nums) - 1 #boundary: everything RIGHT of r is a 2
        i = 0 #scanner: looks at each unknown element

        while i <= r: #i <= r (not <) because nums[r] hasn't been checked yet
            if nums[i] == 0: #belongs in the front
                nums[i], nums[l] = nums[l], nums[i] #swap it into the 0 section
                l += 1 #the 0 section grew by one
                i += 1 #safe to move on, what we swapped in from l was already examined
            elif nums[i] == 2: #belongs in the back
                nums[i], nums[r] = nums[r], nums[i] #swap it into the 2 section
                r -= 1 #the 2 section grew by one, i stays because the new nums[i] is unchecked
            else: #it's a 1
                i += 1 #1s stay in the middle, move on
        #no return statement needed, we modify nums in place

# 1st Solution Logic:
# The array is split into four zones: [0s | 1s | unknown | 2s], split by l, i and r.
# Everything before l is 0. Between l and i is 1. Between i and r is unknown. After r is 2.
# We only advance i after a 0 or a 1, because the element swapped in from l is always a 1 (already seen).
# After a 2, the element swapped in from r is unknown, so i must stay and check it.
# Tracing [2,0,1]: i = 0 is 2 -> swap with r -> [1,0,2], r = 1. i = 0 is 1 -> i = 1.
# i = 1 is 0 -> swap with l (index 0) -> [0,1,2], l = 1, i = 2. i > r -> done.

#- Time: O(n)  each step either moves i forward or shrinks r, so at most about n steps total.
#- Space: O(1)  three index variables, sorted in place.

# =============================================================================
#26 Remove Duplicates from Sorted Array
# =============================================================================

#1. Restate the problem
#"So we're given a sorted array, and I need to remove the duplicates in place so each value shows up once,
# keep the order, and return k, the number of unique values. The first k spots must hold those values."

#2. Clarifying questions
#Is O(1) extra space strictly required, or would a set / new list be acceptable if it's simpler?
#Should I guard against an empty array even though it may not be in the input, or can I trust the constraints?
#Can I rely on the input being sorted, or should I be defensive if it isn't?

#3. Strategy/method, trade offs
#Two pointers (slow and fast). Fast scans every element; slow is the next slot for a new unique value.
#Since the array is sorted, a new value is just one that's different from the last unique value we kept.
#When fast finds one, copy it to slow and move slow. Final slow = k. O(n) time, O(1) space.
#Using a set would also work and is shorter, but it costs O(n) space, needs a sort afterward to restore the order,
#and ignores the fact that the input is already sorted, so two pointers is cheaper on both time and space.

#4. Edge cases
#Empty array -> return 0.
#Single element -> it's unique, return 1.
#All the same [2,2,2] -> only the first is kept, return 1.
#No duplicates [1,2,3] -> every element gets copied onto itself, return len(nums).

#1st solution- Two Pointers Method
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Time: O(n), Space: O(1)
        if not nums: #empty array has no uniques
            return 0

        slow = 1 #slow pointer: next slot for a new unique value (index 0 is always unique, so start at 1)
        for fast in range(1, len(nums)): #fast pointer: scans every element after the first
            if nums[fast] != nums[slow - 1]: #differs from the last unique value we kept -> it's new
                nums[slow] = nums[fast] #copy it into the slow spot (if slow == fast it copies onto itself, harmless)
                slow += 1 #next unique goes one spot to the right
        return slow #like Remove Element we DO return: slow = k, the number of unique values

# 1st Solution Logic:
# Everything LEFT of slow is the unique values, packed at the front in sorted order.
# nums[slow - 1] is always the last unique value we kept, so comparing against it is how we detect a new value.
# Duplicates are just skipped; they get overwritten later or end up past index k, where we don't care.
# Tracing [0,0,1,1,2]: slow = 1. fast = 1 (0) equals nums[0] -> skip. fast = 2 (1) differs -> nums[1] = 1, slow = 2.
# fast = 3 (1) equals nums[1] -> skip. fast = 4 (2) differs -> nums[2] = 2, slow = 3 -> return 3, nums = [0,1,2,...].

#- Time: O(n)  fast visits each element once.
#- Space: O(1)  only two index variables, nums is modified in place.


#2nd solution- Set + Sort (in case they don't want to rely on the sorted order), simpler but uses extra space
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Time: O(n log n), Space: O(n)
        nums[:] = sorted(set(nums)) #set drops duplicates, sorted restores the order, nums[:] overwrites the ORIGINAL list in place
        return len(nums) #k = number of unique values

# 2nd Solution Logic:
# A set removes duplicates for us, then sorting puts the values back in order.
# nums[:] = ... matters: plain nums = ... would only rebind the local name and the original list wouldn't change.
# This is short and correct, but it ignores that the input is already sorted and breaks the O(1) space requirement,
# so the two pointer solution is the one to lead with.

#- Time: O(n log n)  building the set is O(n), sorting the unique values is O(n log n).
#- Space: O(n)  the set and the sorted list hold up to n values.

