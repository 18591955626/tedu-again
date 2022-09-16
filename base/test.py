# a = b = '赵敏'
# print(a, '~~~~', b)
# print(1.23e-2)


year = int(input("Please enter year:"))

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
	print('the year is leap year')
