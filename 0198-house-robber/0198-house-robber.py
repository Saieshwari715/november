class Solution:
    def rob(self, nums: List[int]) -> int:
        p1=0
        p2=0
        for i in nums:
            c=max(p1,i+p2)
            p2=p1
            p1=c
        return p1