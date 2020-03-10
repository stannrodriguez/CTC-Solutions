"""
Return Kth to Last: Implement an algorithm to find the kth to last element of a singly linked list.
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
	def findKthToLast(self, llist, k):
		n = 0
		tmp = llist
		while tmp:
			n += 1
			tmp = tmp.next
		tmp = llist
		for i in range(n-k):
			tmp = tmp.next
		return tmp.data

ll = list2linkedlist([100,101,102,102,103,104, 105])
print(Solution().findKthToLast(ll, 2))
print(Solution().findKthToLast(ll, 1))
print(Solution().findKthToLast(ll, 5))