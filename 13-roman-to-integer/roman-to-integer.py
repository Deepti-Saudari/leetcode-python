class Solution:
    def romanToInt(self, s: str) -> int:
        d={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        res=0
        for i,v in enumerate(s):
            res+=d[v]
            if i==0:
                continue
            if (s[i-1]=="I" and s[i]=="V") or (s[i-1]=="I" and s[i]=="X"):
                res-=2
            elif (s[i-1]=="X" and s[i]=="L") or (s[i-1]=="X" and s[i]=="C"):   
                res-=20
            elif (s[i-1]=="C" and s[i]=="D") or (s[i-1]=="C" and s[i]=="M"):   
                res-=200
        return res



        