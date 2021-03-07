def Number(user_number):
	if(user_number.isnumeric()):
		return True
	else:
		print("The number you have entered is an invalid number.")
		return False


def getValidValue():
	while(True):
		user_number = input("Please input a positive number.")
		if(checkIfNumber(user_number)):
			user_number = int(user_number)
			return user_number



def decimalToBinary(user_number):
	if (user_number > 1):
		decimalToBinary(user_number // 2)
	print(user_number % 2, end = '')


def main():
	a = 0
	b = 1
	c = 0
	sum = sum + b
	d = 1
	e = 0
	user_number = getValidValue()

while(c < user_number):
	sum = sum + b
	c = b
	b = b + a
	a = c
print("The sum of all Fibonacci numbers less than",  user_number,"is", sum, ".")


if(user_number == 1 or usernumber == 0):
	print(user_number, "is neither prime, nor composite.")
else:
	while(d < user_number//2):
		d = d + 1
		if(user_number % d == 0):
			e = 1
			break
		if(e == 1):
			print(user_number, "is not a prime number.")
		else:
			print(user_number, "is a prime number.")

print("The binary representation of", user_number, "is", end = '')
decimalToBinary(user_number)
print("\n")


main()
