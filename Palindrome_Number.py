class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        return str(abs(x)) == str(abs(x))[::-1] if x >= 0 else False
