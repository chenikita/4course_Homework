# Взять строку '/bin:/usr/bin:/usr/local/bin' и разбить ее в список по символу ':'
a = '/bin:/usr/bin:/usr/local/bin'
# a = list(a)
# a.sort(key = ':')
# print(a)
# b = []
print(a.split(':'))
# def sort():
# for i in a:
# 	for i in a:
# 		if i != ':':
# 			b.append(i)
# 		else:
# 			break
# print(b)
# print(a)
# print(c)
