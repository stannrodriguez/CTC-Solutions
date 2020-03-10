"""
Check Permutation: Given two strings, write a method to decide if one is a permutation of the
other. 
"""

class Solution:
	def checkPermutation(self, s1, s2):
		if len(s1) > len(s2):
			return self.checkPermutationHelper(s1, s2)
		else: 
			return self.checkPermutationHelper(s2, s1)

	def checkPermutationHelper(self, longerS, shorterS):
		l1 = list(longerS)
		for char in shorterS:
			if char in l1:
				l1.remove(char)
			else:
				return False
		return True

print(Solution().checkPermutation('abc', 'abcd'))
print(Solution().checkPermutation('abcd', 'abc'))
print(Solution().checkPermutation('aaa', 'bbb'))
print(Solution().checkPermutation('1234', '4321'))

"""
Time Complexity: O(n) where n <= len(s1), len(s2)
Space Complexity: O(n)
"""

"""
Notes:
1) Ask interviewer is the problem is case sensitive
	- is "God" a permutation of "dog"?
	- if so, run s.lower()
2) Ask if white space is significant
	- is "Stephanie     " a permutation of "Stephanie"?
	- if so, run s.replace(' ', '')
3) Ask if permutations have to be complete or if they can be partial
	- "ab" is technically a permuation of "abc"
	- if so, remove Helper
"""