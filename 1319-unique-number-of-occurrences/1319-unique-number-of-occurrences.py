class Solution:
    def uniqueOccurrences(self, nums: List[int]) -> bool:
        dic={}
        for i in nums:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        for values in dic:
            values=list(dic.values())
        if len(values)==len(set(values)):
            return True
        else:
            return False

        