"""
elete Middle Node: Implement an algorithm to delete a node in the middle (i.e., any node but the first and last node, not necessarily the exact middle) of a singly linked list, given only access to that node.
EXAMPLE
Input: the node c from the linked list a - >b- >c - >d - >e- >f
Result: nothing is returned, but the new linked list looks like a - >b- >d - >e- >f
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
	def deleteMiddleNode(self, llist, node):
		print('Before:', end = ' ')
		printList(llist)

		node.data = node.next.data
		node.next = node.next.next

		print('After:', end = ' ')
		printList(llist)

ll = list2linkedlist(['a','b','c','d','e','f'])
Solution().deleteMiddleNode(ll, ll.next.next)