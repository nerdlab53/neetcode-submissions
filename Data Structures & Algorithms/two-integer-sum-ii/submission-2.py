class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]: 
        res = []
        n = len(numbers)
        for i in range(n):
            k = 0
            while k < n:
                if target - numbers[i] == numbers[k] and k > i:
                    res.append(i+1)
                    res.append(k+1)
                    break
                k += 1
        return res