class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1  # Initialize a variable k to 1, which represents the current length of the modified array.

        for i in range(1, len(nums)):  # Iterate through the array, starting from index 1.
            if nums[i] != nums[i - 1]:  # Check if the current element is not equal to the previous element.
                nums[k] = nums[i]  # Copy the non-duplicate element to the k-th position in the array.
                k += 1  # Increment k to maintain the current length of the modified array.

        return k  # Return k, which represents the length of the modified array with duplicates removed.


# input
# nums = [0,0,1,1,1,2,2,3,3,4]
# Output
# [0,1,2,3,4]
# Expected
# [0,1,2,3,4]
