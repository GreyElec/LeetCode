# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 09:40:42 2018

@author: privacy
"""

class Solution:
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        dic = dict()
        for char in s:
            if char in dic.keys():
                dic[char] += 1
            else:
                dic[char] = 1
        key,count = map(list,zip(*sorted(zip(dic.keys(),dic.values()),key = lambda x:x[-1],reverse = True)))
        ans = ''
        for i in range(len(count)):
            while count[i] != 0:
                ans += key[i]
                count[i] -= 1
        return ans
        
S = Solution()
print(S.frequencySort('aabbbc'))