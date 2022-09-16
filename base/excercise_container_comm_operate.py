# str1= '悟空'
# str2 = '八戒'
#
# str3 = str1 + str2
#
# print(str3)
#
# str4 = str1 * -1
# print(str4)
#
#
# print('Hello' not in 'Hello World')
#
# str5 = 'good good study'
#
# str6 = str5[-1:-3]
#
# print(str6)

# str = input('please input str:')
#
# print(str[0])
# print(str[-1])
# print(str[-3])
# print(str[:2])
# print(str[::-1])
#
#
# if len(str) % 2 != 0:
# 	print(str[len(str)//2])

# name = '悟空'
# age = 800
# score =99.5
# print('my is %s,age is %d,score is %.1f'%(name,age,score))


# len_side = int(input('please input length of side:'))
# print('*'*len_side)
# count = 0
#
# while count < len_side-2:
# 	print('*'+' '*(len_side-2)+'*')
# 	count += 1
# print('*'*len_side)

# str = '上海自来水来自海上'
#
# if str == str[::-1]:
# 	print('is palindrome')
# else:
# 	print('is not palindrome')

'''
如果是奇数，len(str)//2, 第一个等于最后一个......, len(str)//2 的不判断。
                       str[0] = str[-1]
                       str[1] = str[-2]
                       str[2] = str[-3]
                       str[3] = str[-4]
'''

# if len(str) % 2 != 0:
# 	for i in range((len(str)//2)):
# 		if str[i] != str[-i-1]:
# 			print('Str is not palindrome')
# 			break
# 		else:
# 			if i+1 == len(str)//2:
# 				print('Str is palindrome')
# 				print('aaa')
# else:
# 	for i in range(int(len(str) / 2)+1):
# 		if str[i] != str[-i - 1]:
# 			print('Str is not palindrome')
# 			break
# 		else:
# 			if i == int(len(str) / 2):
# 				print('Str is palindrome')
# 				print('aa')
			

max_altitude = 100
min_altitude = 0.01

"""
100 up 50
50 up 25
25 up 12.5
"""
distance = max_altitude
count = 0

while max_altitude / 2 > min_altitude :
	distance += max_altitude
	max_altitude /= 2
	count += 1
print(distance)
print(count)









