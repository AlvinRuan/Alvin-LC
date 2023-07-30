class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        collection_of_anagrams = {}
        for i in strs:
            sorts = "".join(sorted(i))
            if sorts in collection_of_anagrams:
                collection_of_anagrams[sorts] += [i]
            else:
                collection_of_anagrams[sorts] = [i]
        result = []
        for i in collection_of_anagrams:
            result.append(collection_of_anagrams[i])
        return result