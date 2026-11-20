class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        totals = dict()

        for word in strs:
            ordered = "".join(sorted(word))
            totals.setdefault(ordered, []).append(word)
        
        return list(totals.values())