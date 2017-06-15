# Создать список с тремя значениями 'to-delete' и нескольми любыми другими, удалить из него 
# все значения 'to-delete'

to_del  = ['to-delete', 123, str, float, 'to-delete', 'smth', [1,2,3,4,5], 'to-delete']

for i in to_del:
	if i == 'to-delete':
		to_del.remove(i)
print(to_del)