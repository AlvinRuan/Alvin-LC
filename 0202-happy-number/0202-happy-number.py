class Solution:
    def isHappy(self, n: int) -> bool:
        
        
        # if sum is 1, return true
        # else (for each digit in sum) - recursively search a number - condition is if its a 1 OR 

        hashmap = set()

        # while number does not equal 1
        while n != 1:
            if n in hashmap:
                return False
            hashmap.add(n)
            newN = 0
            for i in str(n):
                newN += int(i)**2
            n = newN
        return True