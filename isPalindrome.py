# Solution 1
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        palindrome = ""
        for letter in s:
            if letter.isalnum():
                palindrome += letter
        if palindrome == palindrome[::-1]:
            return True
        return False

# Solution 2
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        palindrome = ""
        for letter in s:
            if letter.isalnum():
                palindrome += letter
        l, r = 0, len(palindrome) - 1
        while l < r:
            if palindrome[l] == palindrome[r]:
                l += 1
                r -= 1
            else:
                return False
        return True