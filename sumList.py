numList = [0, 4, 17, 10, 5]
def sumList(numbers):
	sum = 0
	if len(numbers) == 0:
		return sum
	else:
		sum += numbers[0]
		return sum + sumList(numbers[1:])
	
		
		
print(sumList(numList))

	