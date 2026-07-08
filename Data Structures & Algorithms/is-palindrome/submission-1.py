class Solution:
    def isPalindrome(self, s: str) -> bool:
        _s = ''.join(i.lower() for i in s if i.isalnum())
        return _s == _s[::-1]