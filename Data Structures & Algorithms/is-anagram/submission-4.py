class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sCounts = dict();
        tCounts = dict();
        sLength = len(s)
        if sLength != len(t):
            return False
        
        for i in range(sLength):
            if s[i] in sCounts:
                sCounts[s[i]] += 1
            else:
                sCounts[s[i]] = 1

            if t[i] in tCounts:
                tCounts[t[i]] += 1
            else:
                tCounts[t[i]] = 1

        return sCounts == tCounts