class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        results = []

        for anagram in strs:
            if not results:
                results.append([anagram])
                continue

            flag = False

            for i, result in enumerate(results):
                if sorted(anagram) == sorted(result[0]):
                    results[i].append(anagram)
                    flag = True
                    break

            if not flag:
                results.append([anagram])

        return results