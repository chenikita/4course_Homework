# Пройти по всем числам от 1 до 100, написать в консоль, какие из них делятся на 7, 
# а какие - нет

for i in range(1, 100):
	if i % 7 == 0:
		print('and {} is!'.format(i))
	else:
		print('{} is not multiple of 7'.format(i))