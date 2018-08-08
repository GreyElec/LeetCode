# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 16:09:17 2018

@author: privacy
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        stack = []
        while head:
            stack.append(head)
            head = head.next
        if n == len(stack):
            stack.pop(0)
            return stack[0] if stack else []
        if n == 1:
            stack.pop()
            if stack:
                stack[-1].next = None
                return stack[0]
            else:
                return []
        else:
            stack[-(n+1)].next = stack[-(n-1)]
            return stack[0]
        
# the above is my dirty solution
            '''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        current = head
        runner = head
        
        nApart = 0
        while(nApart<n):
            runner = runner.next
            nApart = nApart + 1
        
        if(runner==None):
            return head.next
        
        while(runner.next!=None):
            current = current.next
            runner = runner.next
        
        current.next = current.next.next
        return head
        
'''
# this solution uses the two pointer, really beautiful