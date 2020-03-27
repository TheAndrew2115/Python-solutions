import collections

'''
Given an array of strings, return a list of anagram groups.
Ex: ["eat","tea","nat","tan"]
Output: [["eat","tea"],["nat","tan"]]
'''

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        ourdict = collections.defaultdict(list)
        for s in strs:
            ourdict[tuple(sorted(s))].append(s)
        return ourdict.values()

s = Solution
print(s.groupAnagrams(s, ["eat", "tea", "tan", "ate", "nat", "bat"]))
