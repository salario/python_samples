def collatz(number):
	while number != 1:
		if number % 2 == 0:
			return number // 2
		elif number % 2 == 1:
			return number * 3 + 1

print('Enter a number.')
userNum = int(raw_input())

while collatz(userNum) != 1:
	print(collatz(userNum))
	userNum = collatz(userNum)
	continue
	print(collatz(userNum))
	break

print(collatz(userNum))
print('Nice work, Salar!')