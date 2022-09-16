# import random
#
# score = 0
# for i in range(3):
# 	first_num = random.randint(1,100)
# 	second_num = random.randint(1,100)
# 	sum = first_num + second_num
# 	input_value = int(input('please input result:'+str(first_num)+'+'+str(second_num)+'='))
#
# 	if input_value == sum:
# 		print('good，got 10 score')
# 		score += 10
# print('total score:',score)

sum_value = 0
for item in range(10,51):
	if item % 10  not in (2,5,9):
		print(item)
		sum_value += item
print(sum_value)


