class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        f = 0
        s = 1
        i = 0
        while i < n:
            f,s = s,f+s
            i = i + 1
        return s
