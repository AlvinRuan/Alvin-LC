class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        
        arr = [pref[0]]
        
        for i in range(1,len(pref)):
            print(i)
            arr.append(pref[i] ^ pref[i-1])
        # arr[0] ^ pref[0] = x
        # 2 = pref
        return arr