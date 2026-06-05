class Solution(object):

    def isPalindrome(self, x):
        temp = x
        rev = 0

        while temp != 0:
            d = temp % 10
            rev = rev * 10 + d
            temp = temp // 10

        return rev == x

    def check(self, n, k):

        for i in range(10**n - 1, 10**(n - 1) - 1, -1):

            if self.isPalindrome(i):

                if i % k == 0:
                    return i
