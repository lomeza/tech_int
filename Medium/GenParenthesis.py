class GenParenthesis:
    def generateParenthesis(self, n):
        stack = []
        res = []

        def backtrack(openN, closedN):
            #append to res & return if there are as many open and closed parenthesis as n
            if openN == closedN == n:
                res.append("".join(stack))
                return
            #if there are less open than n append and use recursion to increment and pop 
            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)
                stack.pop()
            #if there are less closed than open append and use recursion to increment and pop 
            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()
        
        backtrack(0, 0)
        return res