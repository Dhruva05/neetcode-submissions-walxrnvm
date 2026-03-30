class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        if len(strs) == 0:
            return []

        for i in range(len(strs)):
            groups.setdefault("".join(sorted(strs[i])), []).append(strs[i])
    
        return list(groups.values())