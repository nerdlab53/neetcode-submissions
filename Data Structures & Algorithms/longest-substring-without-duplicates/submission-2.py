class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        n = len(s)
        left = 0
        seen = set()
        max_len = 0
        for right in range(n):
            while s[right] in seen:
                seen.discard(s[left])
                left += 1
            seen.add(s[right])
            max_len = max(max_len, len(s[left:right])+1)
        return max_len