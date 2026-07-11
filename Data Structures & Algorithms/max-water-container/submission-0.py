class Solution:
    def maxArea(self, heights: List[int]) -> int:
        if not heights:
            return 0
        n = len(heights)
        l = 0
        r = n - 1
        am = 0
        while l < r:
            ca = min(heights[l], heights[r]) * (r - l)
            am = max(am, ca)
            if heights[l] < heights[r]:
                l+=1
            else:
                r-=1
        return am