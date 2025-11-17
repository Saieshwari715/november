class Solution:
    def hammingWeight(self, n: int) -> int:
        b=bin(n)
        c=0
        for i in range(2,len(b)):
            if(b[i]=='1'):
                c+=1
        return c

        