import sys

def check_divisibility(num):
	if num % 15 == 0:
		return "fizzbuzz"
	elif num % 3 == 0:
		return "fizz"
	elif num % 5 == 0:
		return "buzz"
	else:
		return num

for i in range(1, len(sys.argv)):
	print(check_divisibility(int(sys.argv[i])))