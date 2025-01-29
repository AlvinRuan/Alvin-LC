class Solution:
    def isValid(self, s: str) -> bool:


        stack = []

        pairs = {
            "}" : "{",
            ")" : "(" ,
            "]" : "[" 
        }

        for i in s:
            if i in pairs:
                if len(stack) > 0:
                    popped = stack.pop()
                    if pairs[i] != popped:
                        return False
                else:
                    return False
            else:
                stack.append(i)
        
        if len(stack) != 0:
            return False
        else:
            return True
                
            