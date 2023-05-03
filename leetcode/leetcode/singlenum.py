class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        numn = 0 #4
        for x in nums:
            numn ^= x
        return numn