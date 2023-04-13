# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:  
        def traverse(list):
            temp=list
            intdata=""
            while temp is not None:
                intdata += str(temp.val)
                temp = temp.next
            return intdata
        l1Num = traverse(l1)[::-1]
        l2Num = traverse(l2)[::-1]
        sum = int(l1Num) + int( l2Num)
        sum = str(sum)[::-1]
        l3 = prevnode= ListNode(sum[0])
        for i in range(1,len(sum)): 
            newnode= ListNode(sum[i])
            prevnode.next = newnode
            prevnode = newnode
            
        return l3
                
