
#Dynamic Programmming: Top-Down Memoization, Bottom Up Tabulation

Top-Down (Memoization): Big problem → recurse down → cache (function remembers its values) to reuse answers to solve subproblems
Bottom-Up (Tabulation): Base cases → loop up → fill DP table/array until you reach the final answer.
#cache in Python stores previously computed function results so when the same function gets repeatedly called, we can use our saved answer

from functools import cache

def top_down(n):

    @cache
    def dp(i):

        if i <= 1:                   # Base case: Where recursion stops; returns the known answer for the smallest subproblems.
            return 1

        return dp(i - 1) + dp(i - 2) # Transition: Calculates the current subproblem using recursive calls to smaller subproblems.

    return dp(n)                     # Start state: Calls dp() with the full problem, recursively breaking it down until it reaches the base cases.


def bottom_up(n):

    dp = [1] * (n + 1)               # Initialize table / base cases: Creates a DP array and fills in the known answers for the smallest subproblems.

    for i in range(2, n + 1):        # Builds answers from smallest to largest.

    dp[i] = dp[i - 1] + dp[i - 2] # Transition: Calculates the current subproblem using previously computed answers in the table.
    
return dp[n]                   # Final answer: Returns the DP entry for the full problem.









