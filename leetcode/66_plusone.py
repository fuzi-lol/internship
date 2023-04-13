class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = int("".join(list(map(str,digits))))
        num+=1
        l= list(map(int,list(str(num).strip())))
        return l
