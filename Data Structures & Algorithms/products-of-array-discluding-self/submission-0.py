class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if not nums:
            return 0
        p = [0] * len(nums)
        for i in range(len(nums)):
            s = 1
            for j in range(len(nums)):
                if i == j:
                    continue
                s *= nums[j]
            p[i] = s
        return p