class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        dict={}
        for i in nums:
            if i in dict:
                dict[i]+=1
            else:
                dict[i]=1
        for key,values in dict.items():
            if(values==1):
                return key
        