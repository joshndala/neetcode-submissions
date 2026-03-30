class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        listNums = []

        for i in nums:
            print(i)
            if i in listNums:
                return True
            else:
                listNums.append(i)

        return False