class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #only add open parenthesis if open < n
        #only add a closing parenthesis if closed < open
        #stop when open == closed == n

        stack = []
        res = []

        def backtrack(openN, closedN):
            if openN == closedN == n:
                res.append("".join(stack))
                return

            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)
                stack.pop() #there's only a single global stack variable

            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()

        backtrack(0, 0)
        
        return res