class ValidParentheses:
    def pIsValid(self, s: str) -> bool:
        
        stackList = []
        closeSymb={"]" : "[", ")":"(", "}":"{"}
        
        # outter loop to check all chars in string
        for char in s:               
            # checking based on the close char in the dict
            if char in closeSymb:
                # if the stack matches the dict then remove from stack
                if stackList and stackList[-1] == closeSymb[char]:
                    stackList.pop()
                # if order is incorrect then return false
                else:
                    return False
            # add each char to the stack
            else:
                stackList.append(char)
        # if stack is empty at the end then all parentheses are correct
        return True if not stackList else False