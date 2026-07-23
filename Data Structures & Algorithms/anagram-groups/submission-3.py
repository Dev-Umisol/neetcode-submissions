class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        for c in strs:
            sorted_string = ''.join(sorted(c))
            result[sorted_string].append(c)
        
        return list(result.values())