#https://leetcode.com/problems/valid-palindrome/
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


        #Reversing the string using string slicing [::-1]
        #1st)start with empty string since(''.join()) to combine chracters into one string without spaces
        #do conversion inside- convert the characters to lowercase
        # follow that with list comphrension check if c is alphanumeric
        # if statment comaprsion between new string and reversed string return true if not false

        #""new_s=''.join(c.lower) for c in s if c.isalnum(())
        #if new_s== new_s[::-1]:
        #  return False
        #return True



#you can also do reversing the string with string slicing-

class Solution:
    def isPalindrome(self, s: str) -> bool:
        #use list comprehension to create a new string
        new_string = ''.join(c.lower() for c in s if c.isalnum())

        if new_string != new.string[::-1]:
            return False
        return True

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Create a new string using .join() on empty seperate '' to combine characters without spaces
        # and use list comprension inside, our expression convert characters to lowercase then our for loop if condition keep only alphanumeric characters
        

        # Comparison check: Compare normal strings to reversed string, return False if they don't match
        if new_string != new_string[::-1]:
            return False

        # If they match, return True
        return True


class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_string = ''.join(c.lower() for c in s if c.isalnum())
        #new_list = [expression for item in iterable if condition]
        
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
            
        
