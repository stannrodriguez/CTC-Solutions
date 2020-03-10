"""
Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you
cannot use additional data structures? 
"""

class Solution:
	def isUnique(self, s):
		chars = []
		for char in s:
			if char in chars:
				return False
			else: 
				chars.append(char)
		return True

print(Solution().isUnique('abcd'))
print(Solution().isUnique('aaaa'))
print(Solution().isUnique(''))