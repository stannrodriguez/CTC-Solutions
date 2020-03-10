"""
String Rotation; Assume you have a method isSubstring which checks if one word is a substring
of another. Given two strings, si and s2, write code to check if s2 is a rotation of si using only one
call to isSubstring [e.g., "waterbottle " is a rotation of 'erbottlewat")
"""

class Solution:
	def stringRotation(self, s1, s2):
		for i in range(len(s1)):
			if s1[i:] + s1[:i] == s2:
				print(s1[i:] + s1[:i])
				return True
		return False

print(Solution().stringRotation('waterbottle', 'erbottlewat'))