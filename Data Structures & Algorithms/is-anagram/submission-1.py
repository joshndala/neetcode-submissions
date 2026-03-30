class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        count1 = [0] * 26
        count2 = [0] * 26

        for c in s:
            count1[ord(c) - ord("a")] += 1

        for c in t:
            count2[ord(c) - ord("a")] += 1

        if count1 != count2:
            return False
            
        return True