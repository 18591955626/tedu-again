import random

# number = random.randint(1,100)
# print(number)
# input_number = int(input('please input number:'))
# count =0
# while input_number != number:
# 	if input_number > number:
# 		print('input number is too large')
# 		input_number = int(input('please input number:'))
# 	else:
# 		print('input number is too small')
# 		input_number = int(input('please input number:'))
# 	count +=1
# print(count)


# number = random.randint(1, 100)
#
# count = 0
# while True:
# 	count += 1
# 	input_number = int(input('Please input number:'))
# 	if input_number > number:
# 		print('input number is too large')
# 	elif input_number < number:
# 		print('input number is too small')
# 	else:
# 		print('excellent, total guess', count, 'times')


number = random.randint(1,100)

count = 0

while count < 3:
	count += 1
	input_number = int(input('please input number:'))
	if input_number > number:
		print('input number is too large')
	elif input_number < number:
		print('input number is too small')
	else:
		print('excellent, total guess',count,'times')
		break
else:
	print('total guess',count,'times.Game Over')