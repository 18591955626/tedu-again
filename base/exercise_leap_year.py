day = None
# year = int(input('please input year:'))
#
# if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
# 	day = 29
# 	print(day)
# else:
# 	day = 28
# 	print(day)

day = 29 if (int(input('please input year:'))%4 ==0 and int(input('please input year:'))% 100!=0) or int(input('please input year:'))%400 ==0 else 28

print(day)