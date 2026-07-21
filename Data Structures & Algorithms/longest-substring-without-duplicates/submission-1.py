class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0

        for i in range(len(s)):
            c = set()

            for j in range(i, len(s)):
                if s[j] in c:
                    break
                c.add(s[j])
            
            result = max(result, len(c))
        return result