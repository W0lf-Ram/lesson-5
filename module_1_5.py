immutable_var = (1, 2.5, 'string', True)
print('Кортеж: ', immutable_var)
#immutable_var[3] = 'fool'
#Кортеж является неизменяемым объектом и не поддерживает обращение по элементам
mutable_list = [2, 3.5, 'text', False]
mutable_list[1::2] = [5.5, True]
print('Изменённый список: ', mutable_list)