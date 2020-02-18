class Calc():
	def __init__(self):
		self.history = []
		print("You created calc")


	def sum(self, listOfNumbers):
		x = 0
		for item in listOfNumbers:
			x += item
		return x



calc = Calc()
x = calc.sum([1,2,3,34,5,6])
print(x)