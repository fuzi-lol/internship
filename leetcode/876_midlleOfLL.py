# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        size = 0
        while temp is not None:
            size += 1
            temp = temp.next

        if size%2 !=0:
            nthIndex = (size+1)//2
        else:
            nthIndex = (size//2)+1
        temp = head
        for i in range(1,nthIndex):
            temp = temp.next
        head = temp
        return head
