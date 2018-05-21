"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""

class Solution:
    # @param A: Given an integer array with no duplicates.
    # @return: The root of max tree.
    def maxTree(self, A):
        # write your code here
        stack = []
        for ele in A:
            tn = TreeNode(ele)
            while len(stack) and ele > stack[-1].val:
                tn.left = stack.pop()
            if len(stack):
                stack[-1].right = tn
            stack.append(tn)
        return stack[0]