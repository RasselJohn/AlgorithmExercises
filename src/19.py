# Given an integer array nums, move all 0's to the end of it
# while maintaining the relative order of the non-zero elements.
#
# Note that you must do this in-place without making a copy of the array.
#
# Example 1:
# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
#
# Example 2:
# Input: nums = [0]
# Output: [0]

def move_zeroes(nums: list[int]):
    nums_count = len(nums)

    for n in range(nums_count - 1, -1, -1):
        if nums[n] != 0:
            continue

        for i in range(n + 1, nums_count):
            if nums[i] == 0:
                break

            nums[n], nums[i] = nums[i], nums[n]
            n = i
