class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        n = len(height)
        l = 0
        r = n - 1
        w = 0
        lm = height[l]
        rm = height[r]
        while l < r:
            if lm < rm:
                l += 1
                lm = max(lm, height[l])
                w += lm - height[l]
            else:
                r -= 1
                rm = max(rm, height[r])
                w += rm - height[r]
        return w