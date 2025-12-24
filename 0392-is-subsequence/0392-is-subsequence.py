class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s=list(s)
        for i in range(len(t)-1,-1,-1):
            if len(s)>0 and t[i]==s[-1]:
                s.pop()
        return len(s)==0