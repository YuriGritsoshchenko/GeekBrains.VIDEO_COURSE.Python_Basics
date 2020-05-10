"""
1:Даны два произвольные списка.
Удалите из первого списка элементы присутствующие во втором списке.
Примечание.
Списки создайте вручную, например так:
my_list_1 = [2, 5, 8, 2, 12, 12, 4]
my_list_2 = [2, 7, 12, 3]
"""
# my_list_1 = [2, 5, 8, 2, 12, 12, 4]
# my_list_2 = [2, 7, 12, 3]
# print(set(my_list_1) - set(my_list_2))

# my_list_1 = [2, 5, 8, 2, 12, 12, 4]
# my_list_2 = [2, 7, 12, 3]
# for number in my_list_1:
#     if number in my_list_2:
#         my_list_1.remove(number)
#
# print(my_list_1)

my_list_1 = [2, 5, 8, 2, 12, 12, 4]
my_list_2 = [2, 7, 12, 3]
for number in my_list_1[:]:
    if number in my_list_2:
        my_list_1.remove(number)

print(my_list_1)

"""
2:Дана дата в формате dd.mm.yyyy,
например: 02.11.2013.
Ваша задача — вывести дату в текстовом виде,
например: второе ноября 2013 года.
Склонением пренебречь (2000 года, 2010 года)
"""
date = '02.11.2013'
d, m, y = date.split('.')
print(d, m, y)

mounts = {
    '01': 'января',
    '02': 'февраля',
    '03': 'марта',
    '04': 'апреля',
    '05': 'мая',
    '06': 'июня',
    '07': 'июля',
    '08': 'августа',
    '09': 'сентября',
    '10': 'октября',
    '11': 'ноября',
    '12': 'декабря'
}
days = {
    '01': 'первое',
    '02': 'второе',
    '03': 'третье',
    '04': 'четвёртое',
    '05': 'пятое',
    '06': 'шестое',
    '07': 'седьмое',
    '08': 'восьмое',
    '09': 'девятое',
    '10': 'десятое',
    '11': 'одиннадцатое',
    '12': 'двеннадцатое',
    '13': 'тринадцатое',
    '14': 'четырнадцатое',
    '15': 'пятнадцатое',
    '16': 'шестнадцатое',
    '17': 'семнадцатое',
    '18': 'восемнадцатое',
    '19': 'девятнадцатое',
    '20': 'двадцатое',
    '21': 'двадцать первое',
    '22': 'двадцать вторе',
    '23': 'двадцать третье',
    '24': 'двадцать четвёртое',
    '25': 'двадцать пятое',
    '26': 'двадцать шестое',
    '27': 'двадцать седьмое',
    '28': 'двадцать восьмое',
    '29': 'двадцать девятое',
    '30': 'тридцатое',
    '31': 'тридцать первое'
}

result = f'{days[d]} {mounts[m]} {y} года'
print(result)

"""
3:Дан список заполненный произвольными целыми числами.
Получите новый список, элементами которого будут только уникальные элементы исходного.
Примечание. Списки создайте вручную, например так:
my_list_1 = [2, 2, 5, 12, 8, 2, 12]
В этом случае ответ будет:
[5, 8]
"""
my_list_1 = [2, 2, 5, 12, 8, 2, 12]

result = []
for number in my_list_1:
    if my_list_1.count(number) == 1:
        result.append(number)
print(result)
