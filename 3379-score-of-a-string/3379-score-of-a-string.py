class Solution:
    def scoreOfString(self, s: str) -> int:
        a=[]
        for ch in range(1,len(s)):
            d=abs(ord(s[ch-1])-ord(s[ch]))
            a.append(d)
        return sum(a)