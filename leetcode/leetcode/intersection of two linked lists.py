
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        temp1 = headA
        temp2 = headB
        while temp1 != temp2:
            temp1 = temp1.next if temp1 else headB
            temp2 = temp2.next if temp2 else headA
        return temp1
        # intersectedNode = None
        # while temp1 is not None:
            
        #     while temp2 is not None:
        #         count =0
        #         if temp1.val == temp2.val:
        #             intersectedNode = temp2
        #             count=1
        #             break
                    
        #         temp2 = temp2.next
        #     if count ==1:
        #         break

        #     temp1 = temp1.next
        # return intersectedNode
        
        # for j in range(skipB):
        #     print(temp2.val)
        #     temp2 = temp2.next