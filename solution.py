class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        upperBound = len(nums) - 1
        for i in range(upperBound, -1, -1):
            if i == 0:
                nums.sort()
                return
            if nums[i] > nums[i-1]:
                for j in range(upperBound, i - 1, -1):
                    if nums[j] > nums[i-1]:
                        nums[j], nums[i-1] = nums[i-1], nums[j]
                        break
                nums[i:] = sorted(nums[i:])
                return
        """
        Do not return anything, modify nums in-place instead.
        """
        
