class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:  # If the list is empty, return 0
            return 0

        k = 1  # variable to track the number of unique elements

        # Iterate over each element starting from index 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                # If the current element is different from the previous element,
                # move it to the left side of the list
                nums[k] = nums[i]
                k += 1

        return k

[
