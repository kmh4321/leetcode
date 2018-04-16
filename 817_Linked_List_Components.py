#Problem here: https://leetcode.com/problems/linked-list-components/description/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def numComponents(self, head, G):
        """
        :type head: ListNode
        :type G: List[int]
        :rtype: int
        """
        g = set(G)
        ans = 0
        while head:
            if(head.val in g and (head.next == None or head.next.val not in g)):
                ans = ans + 1
            head = head.next
        return ans