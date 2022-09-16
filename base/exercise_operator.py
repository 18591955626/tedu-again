num_one = input('please input first number:')
operator = input('please input operator:')
num_two = input('please input second number:')

if operator == '+':
	print('result:', int(num_one) + int(num_two))
elif operator == '-':
	print('result:', int(num_one) - int(num_two))
elif operator == '*':
	print('result:', int(num_one) * int(num_two))
elif operator == '/':
	print('result:', int(num_one) / int(num_two))
else:
	print('operator is error')
