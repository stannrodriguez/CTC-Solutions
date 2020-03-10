"""
Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palindrome. A palindrome is a word or phrase that is the same forwards and backwards. A permutation
is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words. 
"""

class Solution:
	def palindromePermutation(self, s):
		s = s.replace(' ', '').lower()

		# Build dictionary of counts for each value
		d = {}
		for char in s:
			if char in d:
				d[char] += 1
			else:
				d.update({char: 1})

		# Check if string is palindrome
		if len(s) % 2 == 0:
			return self.checkEven(d)
		else:
			return self.checkOdd(d)

	def checkEven(self, d):
		for count in d.values():
			if count % 2 == 0:
				continue
			else:
				return False
		return True

	def checkOdd(self, d):
		oddCounter = 0
		for count in d.values():
			if count % 2 == 0:
				continue
			else:
				oddCounter += 1
			if oddCounter > 1:
				return False
		return oddCounter == 1

print(Solution().palindromePermutation('Tact Coa'))
print(Solution().palindromePermutation(''))
print(Solution().palindromePermutation('abcba'))
print(Solution().palindromePermutation('Test'))