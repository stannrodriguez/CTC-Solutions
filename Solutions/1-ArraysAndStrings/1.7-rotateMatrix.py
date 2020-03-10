"""
Rotate Matrix: Given an image represented by an NxN matrix, where each pixel in the image is 4
bytes, write a method to rotate the image by 90 degrees.
"""

class Solution:
	def rotateMatrix(self, m):
		"This solution creates a new rotated matrix"
		return [[row[i] for row in m[::-1]] for i in range(len(m))]

print(Solution().rotateMatrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))