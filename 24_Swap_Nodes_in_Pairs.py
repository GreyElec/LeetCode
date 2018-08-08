# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 16:37:08 2018

@author: privacy
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head):
        if not head or not head.next:
            return head        
        pre = dummyHead = ListNode(0)
        while head and head.next:
            nxt = head.next.next
            pre.next = head.next
            head.next.next = head
            pre = head
            head.next = nxt
            head = head.next
        return dummyHead.next

# this question use a assistant pre and nxt variable to conquere the connection problem
# from the last round.