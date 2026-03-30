class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list) # charCount -> anagrams

        for s in strs:
            count = [0] * 26 # a ... z
            
            for c in s:
                count[ord(c) - ord('a')] += 1

            result[tuple(count)].append(s) #tuple bc lists cannot be keys

        return list(result.values())