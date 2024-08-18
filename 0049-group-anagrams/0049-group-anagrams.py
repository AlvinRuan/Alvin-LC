class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        collection = {

        }

        for i in strs:
            alphabetized = ''.join(sorted(i))
            if alphabetized in collection:
                collection[alphabetized].append(i)
                print(collection[alphabetized])
            else:
                collection[alphabetized] = [i]

        result = []

        for i in collection:
            result.append(collection[i])

        return result
            