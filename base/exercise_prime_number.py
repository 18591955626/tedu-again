
number = int(input('please input number:'))

if number > 0:
	for item in range(2,number):
		if number % item == 0:
			print('number is not prime number')
			break
	else:
		print('number is prime number')
else:
	print('input is error')