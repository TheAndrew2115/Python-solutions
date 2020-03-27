import collections

'''
Given a string, return the length of the longest substring that does not contain
repeating characters using the sliding window technique.

Ex: 'bbbbabbbb'
Ans: 2
'''

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 1:
            return 1
        elif s == "":
            return 0
        length = 1
        longestL = 1
        
        ourdict = collections.defaultdict(lambda: 0)
        i = 0;
        j = 0;
        ourdict[s[i]] += 1
        while i < len(s)-1 and j < len(s)-1:
            j += 1
            ourdict[s[j]] += 1
            
            while ourdict[s[j]] > 1:
                if ourdict[s[i]] != 0:
                    ourdict[s[i]] -= 1
                i += 1

            length = j - i + 1
            if length > longestL:
                longestL = length

        return longestL
            

S = Solution
ans = Solution.lengthOfLongestSubstring(S,"bbbabbb")
print(ans)
ans = Solution.lengthOfLongestSubstring(S,"abcabcbb")
print(ans)
ans = Solution.lengthOfLongestSubstring(S,"mynameisjoe")
print(ans)
ans = Solution.lengthOfLongestSubstring(S,"a")
print(ans)
ans = Solution.lengthOfLongestSubstring(S,"abccbcabcccaa")
print(ans)
