class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if not nums:
            return 0
        p = [0] * len(nums)
        pref = [0] * len(nums)
        suff = [0] * len(nums)
        pref[0] = suff[len(nums) - 1] = 1
        for i in range(1, len(nums)):
            pref[i] = pref[i - 1] * nums[i - 1]
        for i in range(len(nums) - 2, -1, -1):
            suff[i] = suff[i + 1] * nums[i + 1]
        for i in range(len(nums)):
            p[i] = pref[i] * suff[i]
        return p