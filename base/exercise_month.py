month = int(input('please input month:'))

if 12 < month or month < 0:
	print('input is error')
elif month == 2:
	print('the month have 28 days')
elif month in (4, 6, 9, 11):
	print('the month hava 30 days')
else:
	print('the month have 31 days')
