class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        totals = dict()
        sorted_strs = sorted(strs)
        for word in sorted_strs:
            ordered = "".join(sorted(word))
            if ordered in totals:
                totals[ordered].append(word)
            else:
                totals[ordered] = [word]
        
        return list(totals.values())