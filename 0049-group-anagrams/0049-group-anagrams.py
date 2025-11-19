class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict={}
        for i in strs:
            j=''.join(sorted(i))
            if j not in dict:
                dict[j]=[]
            dict[j].append(i)
        return list(dict.values())

        