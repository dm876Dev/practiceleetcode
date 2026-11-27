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


