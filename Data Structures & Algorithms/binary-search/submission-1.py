class Solution:
    def search(self, nums: List[int], target: int) -> int:
        pointerA = 0
        pointerB = len(nums) 

        if nums[int(pointerB/2)] == target:
            return int(pointerB/2)
        elif nums[int(pointerB/2)] < target:
            pointerA = int(pointerB/2)
        else:
            pointerB = int(pointerB/2)

        for i in range (pointerA,pointerB):
            if nums[i] == target:
                return i

        return -1