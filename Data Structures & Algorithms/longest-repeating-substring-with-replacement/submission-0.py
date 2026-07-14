class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if not s:
            return 0
        f = {}
        l = 0
        max_len = 0
        max_freq = 0
        for r in range(len(s)):
            f[s[r]] = f.get(s[r], 0) + 1
            max_freq = max(max_freq, f[s[r]])
            while (r - l + 1) - max_freq > k:
                f[s[l]] -= 1
                l += 1
            max_len = max(max_len, r - l + 1)
        return max_len
