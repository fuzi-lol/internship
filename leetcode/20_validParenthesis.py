class Solution:
    
    def check(self,val1,val2):
        return (val1 == '(' and val2 == ')') or (val1 == '[' and val2 == ']') or (val1 == '{' and val2 == '}')

    def isValid(self, s: str) -> bool:       
        stack=[]
        for i in s:
            if i =='[' or i =='(' or i =='{':
                stack.append(i)
            else:
                if len(stack)==0:
                    return False
                if self.check(stack[-1],i):
                    stack.pop()
                    continue
                return 
        if len(stack)==0:
            return True
        return False
                
