class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        
        # Input = string of arrays
        # Output = T/F
        
        # iterate through each variable in the string, we want to see if its a left side of key-value pair or right side - if its left side, add to the end of the stack
        
        
        stack = []

        for i in s:
            if i not in '])}':
                stack.append(i)
            elif len(stack) > 0:
                popped = stack.pop()
                if (popped == '(' and i != ')') or (popped == '[' and i != ']') or (popped == '{' and i != '}'):
                    return False
            else:
                return False
        return False if len(stack) > 0 else True
    