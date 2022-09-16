# score = int(input('please input score:'))
#
# if score > 100 or score < 0:
# 	print('input is error')
# elif 90 <= score <= 100:
# 	print('excellent')
# elif 75 <= score:
# 	print('well')
# elif 60 <= score:
# 	print('pass')
# else:
# 	print('fail')

count = 0
while count<3:
	
	score = input('please input score:')
	if score == '':
		break
	elif int(score) > 100 or int(score) < 0:
		count += 1
		print('input is error')
	elif 90 <= int(score) <= 100:
		print('excellent')
	elif 75 <= int(score):
		print('well')
	elif 60 <= int(score):
		print('pass')
	else:
		print('fail')
else:
	print('error times too much')