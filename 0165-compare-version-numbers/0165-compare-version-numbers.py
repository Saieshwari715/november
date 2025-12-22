class Solution:
    def compareVersion(self, v1: str, v2: str) -> int:
        version1=v1.split(".")
        version2=v2.split(".")
        max_len=max(len(version1),len(version2))
        for i in range(max_len):
            num1=int(version1[i])  if i<len(version1) else 0
            num2=int(version2[i])  if i<len(version2) else 0
    
            if num1>num2:
                return 1
                break
            elif num1<num2:
                return -1
                break
        return 0

        