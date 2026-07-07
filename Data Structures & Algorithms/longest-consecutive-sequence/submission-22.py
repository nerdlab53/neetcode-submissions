class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        s = set(nums)
        fmax = 1
        for num in s:
            if num - 1 not in s:
                _c = num 
                cmax = 1
                while _c + 1 in s:
                    cmax += 1
                    _c += 1
                fmax = max(cmax, fmax)
        return fmax