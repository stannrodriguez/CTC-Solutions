"""
One Away: There are three types of edits that can be performed on strings: insert a character,
remove a character, or replace a character. Given two strings, write a function to check if they are
one edit (or zero edits) away.
EXAMPLE
pale , ple - > true
pales , pale - > true
pale , bale - > true
pale , bake - > false 
"""

class Solution:
	def oneAway(self, s1, s2):
		len1, len2 = len(s1), len(s2)
		if abs(len1 - len2) > 1:
			return False

		if len1 > len2:
			return self.checkAddOne(s1, s2)
		elif len1 < len2:
			return self.checkAddOne(s2, s1)
		else:
			return self.checkEditOne(s1, s2)

	def checkAddOne(self, longerS, shorterS):
		l = list(longerS)
		for char in shorterS:
			if char in l:
				l.remove(char)
			else:
				return False
		return True

	def checkEditOne(self, s1, s2):
		diffCounter = 0
		chars = list(s2)
		for char in s1:
			if char in chars:
				chars.remove(char)
			else:
				diffCounter += 1
			if diffCounter > 1:
				return False
		return True

print(Solution().oneAway('pale', 'ple'))
print(Solution().oneAway('pales', 'pale'))
print(Solution().oneAway('pale', 'bale'))
print(Solution().oneAway('pale', 'bake'))