import os
import random
import re



# friend = 'Максим'
# first_letter = friend[0]
# print('Первая буква имени моего друга', first_letter)
# print('Тип первого символа имени моего друга', type(first_letter))
# first_letter = friend[1]
# print('Вторая буква имени моего друга', first_letter)
#
# print(friend[-1])
# print(friend[-3])

"""friends = 'Максим Леонид1'
print(friends)

print(len(friends))

print(friends.find('Лео'))

print(friends.isdigit())"""

#

"""top5 = 'Первые5 мест на соревнованиях: 1. иванов 2. петров 3. сидоров 4, орлов 5. соколов'
start = top5.find('1')
end = top5.find('4')

top3 = top5[start: end]

result = 'Посдравляем {} с успехом!'.format(top3.upper())
print(result)"""

#

"""friend_name = 'Max'
friends = ['Max', 'Leo', 'Kate']
roles = ('admin', 'quest', 'user')

if 'Max' in friends:
    print('У меня есть этот друг')

if 'M' in friend_name:
    print('Буква М есть в имени друга')

# for

# while

i = 0
while i < len(friends):
    friend = friends[i]
    print(friend)
    i += 1
"""

"""# можно объявить пустой список
empty_list = []

# можно объявить список и сразу заполнить его элементами
friends = ['Max', 'Leo', 'Kate']

# тип списка - list
print(type(friends))

# как и в строке для списка доступны индексы (начинаются с 0)
print('Второй друг: ', friends[1])
print('Первый друг с конца: ', friends[-1])
print('Первый друг: ', friends[0])

# так же можно применить срезы
print(friends[1:2])
print(friends[:2])
print(friends[1:])"""

# Функция len и методы списка

"""friends = ['Max', 'Leo', 'Kate']

print(friends)

print(len(friends))  # длина строки (сколько в ней символов)

friends.append('Ron')

print(friends)
print(len(friends))

print(friends.pop())  # удаление последнего символа
print(friends)

friends.clear()
print(friends)

friends = ['Max', 'Leo', 'Kate']

friends.remove('Kate')  # поиск и удаление в списке символа 'Kate'

del friends[0]  # удаление нулевого, т.е. первого объекта"""

#  Оператор in

"""hero = 'Superman'

if hero.find('man') != -1:
    print('Есть')

if 'man' in hero:
    print('Есть')

goals = ['стать гуру языка python', 'здоровье', 'накормите кота']

if 'здоровье' in goals:
    print('Все хорошо')"""

#  Кортеж - tuple

"""#  Пользователь вводит кол-во участников соревнований по python
#  Пользователь вводит участников и их места в зависимости от кол-ва
#  1. Вывод имен участников по алфавиту
#  2. Получить 3-х победителей и поздравить их
#  3. Победители: ... Поздравляем!

print('СОРЕВНОВАНИЯ ПО PYTHON')
count = int(input('Введите количество участников: \n'))
i = count
members = []
while i > 0:
    name = input('Кто занял {} место: '.format(i))
    members.append(name)
    i -= 1

#  кто участвовал в соревновании (по алфавиту)
print('В соревновании участвовали: ', sorted(members))

#  мы записали людей с конца?
members.reverse()

#  нужно взять первые 3 места
result = members[:3]

result = 'Победители: {}. Поздравляем!'.format(result)
print(result)"""

#  Встроенные типы и операции с ними: Списки; Определение; Методы; Оператор in; Кортежи

"""friend_name = 'Max'
friends = ['Max', 'Leo', 'Kate']
roles = ('admin', 'quest', 'user')

i = 0
while i < len(friends):
    friend = friends[i]
    print(friend)
    i += 1

#  Цикл for

for friend in friends:
    print(friend)

print('end!')


for letter in friend_name:
    print(letter)

print('end!')


for role in roles:
    print(role)

print('end!')"""

#  Функция - range

"""numbers = range(10)
print(numbers)
print(type(numbers))

print(list(numbers))"""

"""winners = ['Max', 'Leo', 'Kate']

#  простой перебор
for winner in winners:
    print(winner)

# используем range
for i in range(len(winners)):
    #  print(i)
    #  print(winners[i])
    #  print(i, ')', winners[i])
    print(i+1, ')', winners[i])"""

#  Параметры range

#  вывести нечетные цифры от 1 до 5

"""numbers = [1, 3, 5]

for number in numbers:
    print(number)

print(list(range(1, 1000, 2)))

for number in range(1, 10, 2):
    print(number)

winners = ['Max', 'Leo', 'Kate']

#  простой перебор
for winner in winners:
    print(winner)

# используем range
for i in range(1, len(winners)+1):
    #  print(i)
    #  print(winners[i])
    #  print(i, ')', winners[i])
    print(i, ')', winners[i-1])

# ВИДЕО НА 46:47 - когда какой цикл использовать

#  СЛОВАРЬ - dict
#  пример:
""""""my_dict = {key1: val1, key2: val2, key3: val3}
dog = {'name': Rocky, age: 3}""""""

friends = ['Max', 'Leo', 'Kate']
print(friends)
print(type(friends))
friend = friends[0]
print(friend)
print(type(friend))

#  как добавить возраст другу?
friend = {
    'name': 'Max',
    'age': 23
}

print(friend)
print(type(friend))

print(friend['age'])

friend['has_car'] = True
print(friend)

friend['has_car'] = False
print(friend)

del friend['age']
print(friend)

if 'has_car' in friend:
    print('Есть машина!')



#  Множества. Методы. Применение

"""
lst = []

for _ in range(10):

    lst.append(random.randint(-10, 10))

# string = "Hello world!"
# print(string[:-2])

# name = 'qwe'
# print(name)
# print(Name)


# print('os.name = ', os.name)
# str = (1, 2, 3, 4)


# string = 'This is a simple test message for test'
# found = re.findall(r'test', string)
# print(found)

