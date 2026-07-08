class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        num = x
        result = 0
        while num > 0:
            last_digit = num % 10
            result = (result * 10) + last_digit
            num //= 10

        return result == x
        