height = int(input('please input your height(cm):'))
weight = int(input('please input your weight(kg):'))

BMI = weight / (height/100) ** 2

if 0 < BMI < 18.5:
	print('weight is low')
elif BMI < 24:
	print('weight iw normal')
elif BMI < 28:
	print('overweight')
	print(BMI)
elif BMI < 30:
	print('first degree obesity')
elif BMI < 40:
	print('seconed degree obesity')
elif 40 <= BMI:
	print('third degree obesity')
else:
	print('life is over')
