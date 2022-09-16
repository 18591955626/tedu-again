
price = int(input("please input price:"))

number = int(input("please input number:"))

paying = int(input("please input paying:"))

give_change = paying - price*number
if give_change > 0:
	print('give change:',give_change)
else:
	print('paying is not enough')