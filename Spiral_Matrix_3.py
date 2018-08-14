# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 09:11:47 2018

@author: privacy
"""

class Solution:
    def spiralMatrixIII(self, R, C, r0, c0):
        """
        :type R: int
        :type C: int
        :type r0: int
        :type c0: int
        :rtype: List[List[int]]
        """
        ans=[[r0,c0]]
        r,c = r0,c0
        direction = [[0,1],[1,0],[0,-1],[-1,0]]
        direct,k = 0,1
        if R*C == 1:
            return ans
        while len(ans) < R*C:
            for _ in range(2):
                direct = direct % 4
                for _ in range(k):
                    r += direction[direct][0]
                    c += direction[direct][1]
                    if 0<=r< R and 0<= c < C:
                        ans.append([r,c])
                direct += 1
            k += 1
        return ans