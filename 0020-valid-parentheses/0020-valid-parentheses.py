class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        
        # Input = string of arrays
        # Output = T/F
        
        # iterate through each variable in the string, we want to see if its a left side of key-value pair or right side - if its left side, add to the end of the stack
        
        
        for i in s:
            if i in '([{':
                stack.append(i)
            
            # if its right side, check the last addition on the stack, and see if it matches the corresponding other side, if not return false, if so, pop the last addition
            elif len(stack) > 0:
                popped = stack.pop()
            
                if (popped == '(' and i != ')') or (popped == '[' and i != ']') or (popped == '{' and i != '}'):
                    return False
            # code block to execute if any of the conditions are True
            else:
                return False

            
        if len(stack) == 0:
            return True
    