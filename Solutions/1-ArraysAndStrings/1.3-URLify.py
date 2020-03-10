"""
URLify: Write a method to replace all spaces in a string with '%20'. You may assume that the string
has sufficient space at the end to hold the additional characters, and that you are given the "true"
length of the string. (Note: If implementing in Java, please use a character array so that you can
perform this operation in place.)
EXAMPLE
Input: "Mr John Smith    "
Output: "Mr%John%20Smith" 
"""

"""
Solution is trivial in python due to replace method for strings
"""

class Solution:
	def URLify(self, s):
		return s.rstrip().replace(' ','%')

print(Solution().URLify('Mr John Smith      '))