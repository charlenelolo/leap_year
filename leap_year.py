
def leap_year(yr):
	int(yr)
	if yr % 4 != 0:
		return('平年')  
	elif yr % 4 == 0 and yr % 100 != 0:
		return('閏年')
	elif yr % 1 == 0 and yr % 400 != 0:
		return('平年')
	elif yr % 400 == 0 and yr % 3200 != 0:
		return('閏年')
	else:
		return('亂寫!')


ly = input('請輸入查詢年分:')
print(leap_year(int(ly)))