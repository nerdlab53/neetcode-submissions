class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        target = sorted(s1)
        m = len(s1)
        for l in range(len(s2) - m + 1):
            if sorted(s2[l:l+m]) == target:
                return True
        return False