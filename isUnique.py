class UniqueTester:
	def __init__(self, stringVal):
		self.strVal = stringVal
		self.arrSize = len(stringVal)
		self.arr = [None] * self.arrSize
		print("Size:",self.arrSize,"Str:",self.strVal,"Arr:",self.arr)
	def h1(self, key):
		return  key % self.arrSize
	def h2(self, key):
		return 2*key + 1
	def hashy(self, key, char, it = 0):
		if it >= self.arrSize:
			return -1 # full
		result = (self.h1(key) + it*(self.h2(key))) % self.arrSize
		if self.arr[result] is None:
			return result
		elif self.arr[result] == char:
			return -1
		else:
			return self.hashy(key, char, it+1)

	def printMe(self):
		print(self.arr)
	def hashify(self):
		for char in self.strVal:
			index = self.hashy(ord(char), char)
			# Testing what index is returned
			print("Index returned:",index)
			if(index == -1):
				return False
			self.arr[index] = char
		return True
	def isUnique(self):
		if self.hashify():
			print("String is composed of unique characters")
		else:
			print("Either the string is not composed of unique characters or this program is trash, take your pick")

def main():
	test = UniqueTester(input("Enter a string: "))
	test.printMe()
	test.isUnique()

main()
