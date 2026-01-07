class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common = ''
        check=set()
        index=0
        shortest = min(strs, key=len)
        for char in shortest:
            for i in range(len(strs)):
                check.add(strs[i][index])
            if len(check)== 1:
                common = common + list(check)[0]
                index +=1
                check=set()
            else:
                return common
        return common
