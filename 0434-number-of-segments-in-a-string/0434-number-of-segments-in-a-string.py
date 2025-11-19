class Solution:
    def countSegments(self, s: str) -> int:
        c=0
        s=s.split()
        for i in s:
            c+=1
        return c
        