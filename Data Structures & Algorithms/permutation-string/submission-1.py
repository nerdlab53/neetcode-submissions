class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        target = sorted(s1)
        r = len(s1)
        for l in range(len(s2) - r + 1):
            if sorted(s2[l:l+r]) == target:
                return True
        return False