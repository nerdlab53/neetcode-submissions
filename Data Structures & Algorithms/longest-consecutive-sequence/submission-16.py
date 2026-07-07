class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = sorted(list(set(nums)))
        if len(s) == 0:
            return 0
        i = 0
        fmax = 1
        cmax = 1
        print(s)
        for i in range(len(s)):
            if s[i-1] == s[i] - 1:
                cmax += 1
            else:
                cmax = 1
            fmax = max(cmax, fmax)
        return fmax