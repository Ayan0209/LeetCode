class Solution:
    def search(self, nums: List[int], target: int) -> int:

        for i, nums in enumerate(nums):
            if nums == target:
                return i
        
        return -1
        
[
