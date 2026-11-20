class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        totals = dict()
        for word in strs:
            ordered = "".join(sorted(word))
            if ordered in totals:
                totals[ordered].append(word)
            else:
                totals[ordered] = [word]
        
        return list(totals.values())