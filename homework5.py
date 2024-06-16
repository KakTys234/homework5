immutable_var = 1, 2, [3, 4], True, 'Hello'
print(immutable_var)
# Нельзя изменить элемент в кортеже, так как элементы в кортеже неизменяемые.
# immutable_var[2] = [5, 8]
# print(immutable_var)
# Но можно
mutable_list = ['Апельсин', 'Мандарин', 23, True]
print(mutable_list)
# Меняем элементы списка
mutable_list[3] = False
mutable_list[0] = 'Яблоко'
mutable_list[2] = 0
print(mutable_list)
