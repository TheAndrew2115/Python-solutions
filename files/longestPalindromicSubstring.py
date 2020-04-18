'''
this is the brute-force solution to finding the largest palindromic substring in the
array
'''

class Solution(object):
    def isPalindrome(self,s):
        if s == '':
            return True
        if s[0] == s[len(s)-1]:
            newS = s[1:len(s)-1]
            return self.isPalindrome(newS);
        return False
    
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 1:
            return s
        elif s == '':
            return None
        ans = ''

        for i in range(0,len(s)-1):
            for j in range(1,len(s)+1):
                newS = s[i:j]
                if len(newS) > len(ans) and self.isPalindrome(newS):
                    ans = newS
        
        return ans

S = Solution()
print(S.longestPalindrome('ababa'))
