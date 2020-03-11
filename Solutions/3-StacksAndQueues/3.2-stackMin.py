"""
Stack Min: How would you design a stack which, in addition to push and pop, has a function min which returns the minimum element? Push, pop and min should all operate in 0(1) time.
"""

class MinStack:
	def __init__(self, data=[]):
		self.data = data
		self.min = min(data, default=None)

	def __str__(self):
		return f'{self.data}'

	def push(self, x):
		if x < self.min:
			self.min = x
		self.data.append(x)

	def pop(self):
		if self.data == []:
			return None
		x = self.data[-1]
		self.data = self.data[:-1]
		if x == self.min:
			self.min = min(self.data)
		print(f'{x}')
		return x

	def get_min(self):
		print(f'{self.min}')
		return self.min

x = MinStack([1,2,3,4,5])
print(x)
x.pop()
print(x)
x.push(1000)
print(x)
x.get_min()