# while True:
# 	season = input('please input season:')
# 	if season == 'Spring':
# 		print('include Jan,Feb,Mar')
# 	elif season == 'Summer':
# 		print('include Apr,May,Jun')
# 	elif season == 'Autumn':
# 		print('include July,Aug,Sep')
# 	elif season == 'Winter':
# 		print('include Oct,Nov,Dec')
# 	else:
# 		print('Input is error')
# 		break

month = int(input('please input month:'))

if month > 12 or month < 1:
	print('input is error')
elif month >= 10:
	print('Winter')
elif month >= 7:
	print('Autumn')
elif month >= 4:
	print('Summer')
else:
	print('Spring')
