# 	Instructions:
# Implement int sqrt(int x).
# Compute and return the square root of x, where x is guaranteed to be a non-negative integer.
# Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.
# Do not use any built square root functions.
def squareRoot(num):
	for i in range(0, num):
		temp = i * i
		if temp == num:
			return i
		elif temp > num:
			return i-1
	
	return -1

sampleInput = 4
print(squareRoot(sampleInput))