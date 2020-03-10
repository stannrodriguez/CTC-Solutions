"""
Remove Dups: Write code to remove duplicates from an unsorted linked list. 
Temporary buffer not allowed.
"""

class Node:
	# Initializing Node object
	def __init__(self, data):
		self.data = data
		self.next = None

def list2linkedlist(l):
	if l == []:
		return None
	head = Node(l[0])
	n = head
	for i in range(1,len(l)):
		new = Node(l[i])
		n.next = new
		n = n.next
	return head

def printList(llist):
	tmp = llist
	while tmp:
		print(tmp.data, end = ' ')
		tmp = tmp.next
	print('')

class Solution:
	def removeDups(self, l):
		seen = []
		llist = list2linkedlist(l)
		tmp = llist
		while tmp:
			#printList(llist)
			if tmp.data in seen and tmp.next:
				# Finds duplicate not at the end of list
				tmp.data = tmp.next.data
				tmp.next = tmp.next.next
			elif tmp.data in seen:
				# Finds duplicate at the end of list
				tmp.data = None
			else:
				# Duplicate not found
				# Add char to seen list + move to next node
				seen.append(tmp.data)
				tmp = tmp.next
		printList(llist)
		return llist

Solution().removeDups([1,1,1,2,3,3,3])
Solution().removeDups([1,1,1])
Solution().removeDups([1,1,1,2,3])