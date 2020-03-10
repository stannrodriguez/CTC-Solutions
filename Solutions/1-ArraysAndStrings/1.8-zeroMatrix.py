"""
Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0, its entire row and
column are set to 0. 
"""

class Solution:
	def zeroMatrix(self, matrix):
		row0 = []
		col0 = []
		n = len(matrix)
		m = len(matrix[0])

		for i in range(n):
			for j in range(m):
				if matrix[i][j] == 0:
					row0.append(i)
					col0.append(j)

		for i in range(n):
			for j in range(m):
				if i in row0 or j in col0:
					matrix[i][j] = 0
	
		return matrix

print(Solution().zeroMatrix([[0,1],[2,3],[4,5],[6,7]]))
print(Solution().zeroMatrix([[1,0,2,3],[4,5,6,7]]))