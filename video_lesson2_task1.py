"""
1:Запросите от пользователя число, сохраните в переменную, прибавьте к числу 2 и выведите результат на экран.
Если возникла ошибка, прочитайте ее, вспомните урок и постарайтесь устранить ошибку.
"""
a = int(input('Пользователь, введите число: '))
print(a + 2)

"""
2:Используя цикл, запрашивайте у пользователя число, пока оно не станет больше 0, но меньше 10.
После того, как пользователь введет корректное число, возведите его в степень 2 и выведите на экран.
Например, пользователь вводит число 123, вы сообщаете ему, что число неверное, и говорите о диапазоне допустимых.
И просите ввести заново.
Допустим, пользователь ввел 2, оно подходит. Возводим его в степень 2 и выводим 4.
"""
"""option_1"""
numb = int(input('Пользователь, введите число, которое > 0, но < 10: '))
if numb <= 0:
    print('Ошибка! Вы ввели число, которое < 0! Смотри условие!')
elif numb >= 10:
    print('Ошибка! Вы ввели число, которое > 10! Смотри условие!')
else:
    print(numb**2)

"""option_2"""
while True:
    numb = int(input('Пользователь, введите число, которое > 0, но < 10: '))
    if numb <= 0 or numb > 10:
        print("Ошибка! Введен неверный диапазон значений! Смотри условие!")
    else:
        break
print(numb**2)

"""
3:Создайте программу “Медицинская анкета”, где вы запросите у пользователя следующие данные:
имя, фамилия, возраст и вес.
Выведите результат согласно которому:
•	Пациент в хорошем состоянии, если ему до 30 лет и вес от 50 и до 120 кг;
•	Пациенту требуется заняться собой, если ему более 30 и вес меньше 50 или больше 120 кг;
•	Пациенту требуется врачебный осмотр, если ему более 40 и вес менее 50 или больше 120 кг;
•	Все остальные варианты вы можете обработать на ваш вкус и полет фантазии.
(Формула не соответствует реальной действительности и здесь используется только ради примера)
Примечание: при написание программы обратите внимание на условия в задаче и в вашем коде.
Протестируйте программу несколько раз и убедитесь, что проверки срабатывают верно.
В случае ошибок, уточните условия для той или иной ситуации.
Пример: Вася Пупкин, 29 год, вес 90 - хорошее состояние
Пример: Вася Пупкин, 31 год, вес 121 - следует заняться собой
Пример: Вася Пупкин, 31 год, вес 49 - следует заняться собой
Пример: Вася Пупкин, 41 год, вес 121 - следует обратится к врачу!
Пример: Вася Пупкин, 41 год, вес 49 - следует обратится к врачу!
"""
name = input('Пользователь, введите Ваше имя: ')
surname = input('Пользователь, введите Вашу фамилию: ')
age = int(input('Пользователь, введите Ваш возраст: '))
weight = int(input('Пользователь, введите Ваш вес: '))
if age <= 30 and 50 <= weight <= 120:
    print(name, surname, ', возраст:', age, 'лет', ', вес:', weight, 'кг.' ' Ваше состояние хорошее!')
elif 30 < age < 40 and (weight < 50 or weight > 120):
    print(name, surname, ', возраст:', age, ', вес: ', weight, '. Вам требуется заняться собой!')
elif 40 < age < 50 and (weight < 50 or weight > 120):
    print(name, surname, ', возраст:', age, ', вес: ', weight, '. Вам необходимо обратиться к врачу!')
