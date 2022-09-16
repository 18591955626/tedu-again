number = int(input('please input number:'))
state = None

if number % 2 == 0:
	state = 'odd'
	print(state)
else:
	state = 'even'
	print(state)

state = 'odd' if int(input('please input number')) % 2 == 0 else 'even'
print(state)


