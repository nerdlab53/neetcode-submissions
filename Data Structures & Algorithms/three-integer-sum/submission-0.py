class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        res = []
        nums.sort()
        n = len(nums)
        for i in range(n):
            k = n - 1
            j = i + 1
            while j < k:
                target = -nums[i]
                if nums[j] + nums[k] < target:
                    j += 1
                elif nums[j] + nums[k] > target:
                    k -= 1
                else:
                    if [nums[i], nums[j], nums[k]] not in res:
                        res.append([nums[i], nums[j], nums[k]]) 
                    j += 1
                    k -= 1
        return res