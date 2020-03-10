"""
String Compression: Implement a method to perform basic string compression using the counts
of repeated characters. For example, the string aabcccccaaa would become a2blc5a3, If the
"compressed" string would not become smaller than the original string, your method should return
the original string. You can assume the string has only uppercase and lowercase letters (a - z). 
"""

class Solution:
	def stringCompression(self, s):
		if len(s) == 0:
			return ''

		answer = ''
		tmp = s[0]
		counter = 1

		for letter in s[1:]:
			if tmp == letter:
				counter += 1
			else:
				answer += tmp + str(counter)
				counter = 1
			tmp = letter
		answer += tmp + str(counter)

		if len(answer) > len(s):
			return s
		else:
			return answer


print(Solution().stringCompression('aabcccccaaa'))
print(Solution().stringCompression('abababs'))

