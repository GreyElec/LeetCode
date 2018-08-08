# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 22:17:00 2018

@author: privacy
"""

class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        Dic,ans = {},[]
        for i in nums:
            if i in Dic.keys():
                Dic[i] += 1
            else:
                Dic[i] = 1
        for ind,val in enumerate(Dic.values()):
            if val == 1:
                ans.append(list(Dic.keys())[ind])
        return ans