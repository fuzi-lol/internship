class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low =0
        high = len(nums)-1
        if (target>nums[-1]):
            return len(nums)
        if(target<nums[0]):
            return 0

        while(low<=high):
            mid =int((low+high)//2)
            if (nums[mid]==target):
                val= mid
                return val
            elif(nums[mid]>target):
                high = mid -1
            else:
                low = mid + 1
                val = low
        return val
        
