#Пицы сделать список из 3х пиц, и при помощи for вывести название каждой на экран
    # - изменить цикл так, что бы выводилось предложение "Я люблю паперони пиццу"

# pizzas = ['paperoni', 'pineapple', 'diablo']
# for pizza in pizzas:
#     print(f"I like {pizza}, pizza")

# додать строку за циклом, о том как сильно я люблю пиццы

# print("I really love pizza")

# сделать список из 3 животных с общей чертой и вывести их через for
    #  - зименить программу так что бы она выводила предложение для каждого животного - A dog would make a great pet
    #    - в конце программы додать вывод строки о том что - Any of these animals would make a great pet

# cats = ['tiger', 'lion', 'jaguar']
# for cat in cats:
#     print(f"A {cat}, would make a great pet")
# print("Any of these animals would make a great pet")

# task2

# при помощи for посчитать до 20 и вывести на экран
# for value in range(21):
#     print(value)

# Сделать список до 1 000 000 и вывести

# for number in range(1_000_001):
#     print(number)

# Сделать списко до 1_000_000. При помощи мин и макс проверить крайние значение.
# Запустить функцию sum

# numbers = list(range(1_000_001))
# print(min(numbers))
# print(max(numbers))
# print(sum(numbers))

# сделать список непарных чисел до 20. через for вывести их

# for i in range(21):
#     if i % 2 != 0:
#         print(i)


# сделать список чисел которые делятся на 3 от 3 до 30, вывести на экран при помощи for

# for i in range(3, 31):
#     if i % 3 == 0:
#         print(i)

# создать список до 10. Возвести их в степень куба

# cubes = []
# for value in range(1, 11):
#     cube = value ** 3
#     cubes.append(cube)

# print(cubes)

# стелать тоже самое через генераторные списки

# cubes = [value**3 for value in range(1, 11)]
# print(cubes)

# my_foods = ['pizza', 'falafel', 'carrot cake', 'cannoli', 'ice cream']
# friend_food = my_foods[:]

# print("My favorite foods are:")
# print(my_foods)

# print("\nMy friends favorite foods are:")
# print(friend_food)

# # вывести сообщение the first three item in the list are и вывести их
# # вывести 3 средних элемента
# # вывести 3 последних элемента


# print(f"The first three items in the list are:{my_foods[:3]}")
# print(f"Three middle items in the list are:{my_foods[1:4]}")
# print(f"Three last items in the list are:{my_foods[2:]}")


# добавить к списку моя еда одну пиццу
# добавить к списку еда друзей одну пиццу
#вывести сообщение моя любимая пицца:, и вывести первый список при помощи for
# вывести сообщение любимая пицца друзей: и вывести второй список

# pizzas = []

# my_foods = ['paperoni', 'pineapple', 'diablo']
# friend_foods = my_foods[:]

# my_food = my_foods.append('margarita')
# print(pizzas)
# print("My favorite foods are:")
# print(my_foods)

# friend_food = friend_foods.append('dour blue')
# print(pizzas)
# print("\nMy friends favorite foods are:")
# print(friend_foods)

# вывести список моя еда при помощи for

# my_foods = ['pizza', 'falafel', 'carrot cake', 'cannoli', 'ice cream']
# friend_food = my_foods[:]  

# print("My favorite foods are:")
# for food in my_foods:
#     print(food)

# print("\nMy friend's favorite foods are:")
# for food in friend_food:
#     print(food)


# в меню ресторана только 5 блюд. Придумать их и сохранить в кортеж 

meal =('coffee', 'tea','cake','pizza','pasta' )
for position in meal:
	print(position)
	
# ресторан обновил меню, заменить две позиции из кортежа

meal = ('coffee', 'tea','cake', 'hotdog', 'burito')
for position in meal:
	print(position)