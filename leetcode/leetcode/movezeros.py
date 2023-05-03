class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i=0
        j=0
        while j< len(nums):
            if nums[j] == 0 :
                j+=1
            else:
                nums[i], nums[j] = nums[j], nums[i]
                j+=1
                i+=1
