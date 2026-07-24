class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        r = n % 4
        if r == 0:
            x = n
        elif r == 1:
            x = 1
        elif r == 2:
            x = n + 1
        else:
            x = 0
        y = 0
        for num in nums:
            y ^= num
        return x ^ y