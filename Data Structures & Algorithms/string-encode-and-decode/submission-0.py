class Solution:

    def encode(self, strs: List[str]) -> str:
        Parts = []
        for s in strs:
            Parts.append(str(len(s)))
            Parts.append("#")
            Parts.append(s)
        return "".join(Parts)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
        
            L = int(s[i:j])
            j += 1
            word = s[j:j+L]
            res.append(word)
            i = j + L
        return res
