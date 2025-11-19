class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums=[]
        x=0
        for i in range(n):
            v=start+2*i
            nums.append(v)
            x^=nums[i]
        return x
        