# Условвия задачи 1
# Будем считать адрес email корректным, если в нём есть символ @ и точки. 
# При этом отсутствуют пробелы. Напишите программу, которая будет 
# проверять корректность адреса email.
# Пример 1
# Пример входных данных:
# helloworld@mail.ru

# Пример ответа:
# True

# Пример 2
# Пример входных данных:
# Hello world@ ya.ru

# Пример ответа:
# False
# На вход программе подаётся строка – адрес email. Программа должна 
# вывести булево значение True, если адрес email является корректным
# и False – в случае некорректного ввода адреса email.

# def check_email(email: str) -> bool:
#     if (email.count('.') != 0) and (email.count('@') != 0) and (email.count(' ') == 0):
#         check = True
#     else:
#         check = False
#     return(check)
# if __name__ == '__main__':
#     assert check_email('Helloworld@.ru') is True
#     assert check_email('мояпочта@нетология.ру') is True
#     assert check_email('python@email@net') is False
#     assert check_email(' em@il.ru') is False
#     print("\nОтличная работа, отправляйте на проверку!")
# check_email('Helloworld@.ru')


# Условие задачи 2
# Даны названия трёх фильмов. Напишите программу, которая определяет 
# самое длинное название фильма.
# 
# На вход программе подаётся названия трёх фильмов. Программа должна
# вернуть самое длинное название фильма.
# 
# Примечание
# Гарантируется, что количество символов в названиях всех трёх фильмов
# не совпадают.
# 
# Пример входных данных:
# Бумер, Мадагаскар, Бетховен
# 
# Пример ответа:
# Мадагаскар

# def longest_film(film_1: str, film_2: str,film_3: str) -> str:
#     # max = film_1
#     # if len(film_2) > len(max):
#     #     max = film_2
#     # elif len(film_3) > len(max):
#     #     max = film_3
#     # return(max)
#     return max(film_1, film_2, film_3, key=len ) # Экспертный вариант
# if __name__ == '__main__':
#     assert longest_film('Аладин', 'Мадагаскар', 'Бетховен') == 'Мадагаскар'
#     assert longest_film('Железный Человек', 'Стражи Галактики 2', 'Капитан Америка') == 'Стражи Галактики 2'
#     assert longest_film('Бумер', 'Бумер: Фильм второй', 'Бумеранг') == 'Бумер: Фильм второй'
#     assert longest_film('Гарри Поттер и философский камень', 'Пираты Карибского моря: На странных берегах',
#                         'ВАЛЛ·И') == 'Пираты Карибского моря: На странных берегах'
#     assert longest_film('Ирония судьбы, или С легким паром!', 'Иван Васильевич меняет профессию ',
#                         'Джентльмены удачи а') == 'Ирония судьбы, или С легким паром!'
#     print("\nОтличная работа, отправляйте на проверку!")

# Условие задачи
# Программе на вход подаётся строка со спецсимволами %% и &# в начале и в конце строки. Напишите программу, которая вернёт строку без спецсимволов.

# Пример входных данных:
# %%Приказ об увольнении&#

# Пример ответа:
# Приказ об увольнении

# def string_slices(string: str) -> str:
#     # return(string.replace('%%','').replace('&#',''))
#     return string[2:-2] # Решение эксперта    
# string_slices("%%Приказ об увольнении&#")
# if __name__ == '__main__':
#     assert string_slices("%%Приказ об увольнении&#") == 'Приказ об увольнении'
#     assert string_slices("%%Лучший студент на курсе!&#") == 'Лучший студент на курсе!'
#     assert string_slices("%%Hello World!&#") == 'Hello World!'
#     print("\nОтличная работа, отправляйте на проверку!")



# from typing import List


# def fio(initials: List[str]) -> str:
#     # return(initials[0][0]+initials[1][0]+initials[2][0])
#     return "".join([initials[0][0], initials[1][0], initials[2][0]]) # Решение эксперта
# if __name__ == '__main__':
#     assert fio(['Иванов', 'Иван', 'Иванович']) == 'ИИИ'
#     assert fio(['Жан', 'Клот', 'Вандамович']) == 'ЖКВ'
#     assert fio(['Павлов', 'Иван', 'Уралович']) == 'ПИУ'
#     assert fio(['Семейный', 'Доминик', 'Торретович']) == 'СДТ'
#     print("\nОтличная работа, отправляйте на проверку!")


# def list_of_numbers(n: int) -> list:
#     # return(list(range(1,n+1)))
#     return list(range(1, n + 1)) # Решение эксперта
# if __name__ == '__main__':
#     assert list_of_numbers(1) == [1]
#     assert list_of_numbers(5) == [1, 2, 3, 4, 5]
#     assert list_of_numbers(9) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
#     print("\nОтличная работа, отправляйте на проверку!")


# def reverse(string: str) -> str:
#     # return string[::-1].lower()
#     return string.lower()[::-1] # Решение эксперта
# if __name__ == '__main__':
#     assert reverse('!dlroW olleH') == 'hello world!'
#     assert reverse('AvadaKedavraaaaA!') == '!aaaaarvadekadava'
#     assert reverse('хаЗерс хишав ХИТЭ в ясларбозар от-ценокан Я') == 'я наконец-то разобрался в этих ваших срезах'
#     print("\nОтличная работа, отправляйте на проверку!")