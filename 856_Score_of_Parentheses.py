class Solution:
    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        """
        stack = []
        for s in S:
            if s =='(':
                stack.append(s)
            else:
                prev = stack.pop()
                if prev == '(':
                    stack.append(1)
                else:
                    currentsum = prev
                    while stack[-1]!= '(':
                        currentsum += stack.pop()
                    stack.pop()
                    stack.append(currentsum*2)
        return sum(stack)