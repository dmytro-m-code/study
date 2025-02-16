#Создание кортежей
my_tuple = (1, 2, 3)
another_tuple = 4, 5, 6
empty_tuple = ()
single_element_tuple = (42,)



print(my_tuple[0])
print(my_tuple[1:3])



my_tuple[0] = 10



new_tuple = (1, 2) + (3, 4) #(1, 2, 3, 4)
repeated = (1, 2) * 3  # (1, 2, 1, 2, 1, 2)



a, b, c = (1, 2, 3)

first, *middle, last = (1, 2, 3, 4, 5)

a, b, *c = ((1, 2), 3, 4, 5, 'something')



len(my_tuple)  # Длина
min(my_tuple)  # Минимум
max(my_tuple)  # Максимум
sum(my_tuple)  # Сумма (если числа)



coords = {(10, 20):"точка A" }
print(coords[(10, 20)])


