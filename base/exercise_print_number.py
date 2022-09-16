start_num = int(input('please input start number:'))
end_num = int(input('please input end number:'))

while start_num > end_num + 1:
	start_num -= 1
	print(start_num)

while start_num < end_num - 1:
	start_num += 1
	print(start_num)
