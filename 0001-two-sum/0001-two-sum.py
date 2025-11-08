class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        hash_map={}
        for i in range(n):
            c=target-nums[i]
            if c in hash_map:
                return[hash_map[c],i]
                break
            hash_map[nums[i]]=i
