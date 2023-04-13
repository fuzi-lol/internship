class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count=0
        for i in range(len(nums)):
            if i==0:
                nums[count]= nums[i]
                prev = nums[i]
                count+=1
            if prev ==nums[i]:
                continue
            else:
                nums[count] = nums[i]
                prev = nums[i]
                count+=1
        return count

            
