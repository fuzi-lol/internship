class Solution:
    def romanToInt(self, s: str) -> int:
        d={"I" : 1, "V": 5, "X" : 10, "L":50,"C":100,"D":500,"M":1000}
        if len(s)==1:
            return d[s[-1]]
        sum=0
        for i in range(0,len(s)-1):
            temp=i+1
            if d[s[i]]<d[s[temp]]:
                
                sum+= d[s[temp]]-d[s[i]]
            
                
            else:
                if d[s[i]]>d[s[i-1]] and i!=0:
                    continue
                sum+=d[s[i]]
        if d[s[-1]]<=d[s[-2]]:
            sum+=d[s[-1]]

        
        return sum

            
