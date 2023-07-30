class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        

        result = {}
        for s in strs:
            key = str(sorted(s))
            if key in result:
                result[key] += [s]
            else:
                result[key] = [s]
        return list(result.values())