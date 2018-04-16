## Problem at : https://leetcode.com/problems/insertion-sort-list/description/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        #Initialize the current node
        #Initialize a counter
        #Initialize a `previous` value
        if(head != None):
	        current_node = head
	        i = 1
	        previous_element = head.val + 1

	        #Run through the entire list once
	        while(current_node.next is not None):
	        	
	        	#Current element to `insert'
	        	current_element = current.val
	        	
	        	#Already sorted
	        	if(current_element <= previous_element):
	        		pass
	        	else:
	        		#Create a temporary node
	        		temp_node = head
	        		j = 0
	        		while(j<=i):
	        			if(temp_node.val<current_element):
	        				temp_node = temp_node.next
	        			else:
	        				to_insert = ListNode(current_element)
	        				to_insert.next = temp_node
	        				break
	        		j = j + 1
	        	previous_element = current_node.val
	        	current_node = current_node.next
	        	i = i + 1
	        head.next = None
        return head