# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 20:44:58 2018

@author: privacy
"""
class Solution:
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        licensePlate = ''.join([i.lower() for i in licensePlate if 65<=ord(i)<=122])
        words.sort(key = len)
        for word in words:
            license = licensePlate
            wordtemp = word
            while license:
                if license[0] in word:
                    word = word[:word.index(license[0])] + word[word.index(license[0])+1:]
                    license = license[1:]
                else:
                    break
            if not license:
                return wordtemp