"""Создать вручную и заполнить несколькими строками текстовый файл,
в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков)."""
import json
companies_data = []
with open("task1.txt", encoding='utf-8') as input_data:
    companies_dict = {}
    profit_list = []
    for company_row in input_data:
        name, form, revenue, costs = company_row.split()
        profit = float(revenue) - float(costs)
        companies_dict[name] = profit
        if profit > 0:
            profit_list.append(profit)
    companies_data.append(companies_dict)
    companies_data.append({"average_profit": round(sum(profit_list) / len(profit_list), 2)})
with open("task2.txt", 'w', encoding='utf-8') as output_data:
    json.dump(companies_data, output_data)
"""Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество.
Важно, чтобы для каждого предмета не обязательно были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран."""
subjects = {}
with open("task2.txt", encoding="utf-8") as file_obj:
    for row in file_obj:
        subject_info = row.split()
        name = subject_info[0].rstrip(":")
        subjects[name] = subject_info[1:]
result = {}
for key, value in subjects.items():
    result[key] = sum([int(hours[:hours.index("(")]) for hours in value if hours != '—'])
print(result)
"""Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран."""
from random import randrange
random_numbers = [randrange(1, 200) for _ in range(50)]
with open("task2.txt", 'w', encoding="utf-8") as input_data:
    input_data.write(" ".join(map(str, random_numbers)))
with open("task2.txt", encoding="utf-8") as output_data:
    numbers = output_data.read().split()
print(sum(int(x) for x in numbers))
"""Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл."""
translation = {'One': "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
converted_rows = []
with open("task2.txt", encoding="utf-8") as input_data:
    for row in input_data:
        name, value = row.split(" — ")
        converted_rows.append(f"{translation[name]} — {value}")
with open("task2.txt", 'w', encoding="utf-8") as output_data:
    output_data.writelines(converted_rows)
"""Создать текстовый файл (не программно),
построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников."""
with open("task2.txt", encoding="utf-8") as file_obj:
    workers_salary = {x.split()[0]: float(x.split()[1]) for x in file_obj}
for key, value in workers_salary.items():
    if value < 20000:
        print(key)
print("Средняя заработная плата", sum(workers_salary.values())/len(workers_salary))
"""Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк, 
количества слов в каждой строке."""
with open("task1.txt") as file_obj:
    rows = file_obj.readlines()
    rows_count, words_count = len(rows), [len(row.split()) for row in rows]
    print(f'Количество строк: {rows_count}, \nКоличество слов в каждой строке: {words_count}')
"""Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка."""
while True:
    with open("task1.txt", 'a+') as file_obj:
            user_input = input("Введите данные строки: ")
            if not user_input:
                break
            file_obj.write(f"{user_input}\n")
"""Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
При вызове функции должен создаваться объект-генератор.
Функция должна вызываться следующим образом: for el in fact(n).
Функция отвечает за получение факториала числа,
а в цикле необходимо выводить только первые n чисел, начиная с 1! и до n!."""
def fact(num):
    factorial = 1
    if num == 0:
        yield factorial
    for x in range(1, num + 1):
        factorial *= x
        yield factorial
factorials = [el for el in fact(5)]
print(factorials)
"""Реализовать формирование списка, используя функцию range() и возможности генератора.
В список должны войти четные числа от 100 до 1000 (включая границы).
Необходимо получить результат вычисления произведения всех элементов списка."""
from functools import reduce
result = [num for num in range(100, 1001, 2)]
print(reduce(lambda x, y: x * y, result))
"""Представлен список чисел. Определить элементы списка, не имеющие повторений.
Сформировать итоговый массив чисел, соответствующих требованию.
Элементы вывести в порядке их следования в исходном списке.
Для выполнения задания обязательно использовать генератор."""
my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result = [num for num in my_list if my_list.count(num) == 1]
"""Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Необходимо решить задание в одну строку."""
print([num for num in range(20, 241) if num % 20 == 0 or num % 21 == 0])
"""Представлен список чисел.
Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента."""
my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result = [el for idx, el in enumerate(my_list) if idx > 0 and my_list[idx-1] < el]
print(result)
"""Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника. В расчете
необходимо использовать формулу: (выработка в часах*ставка в час) + премия. Для выполнения расчета для конкретных
значений необходимо запускать скрипт с параметрами. """
import sys
def salary_func(hours, rate, bonus):
    salary = int(hours) * int(rate) + int(bonus)
    return salary
print(f"Salary: {salary_func(sys.argv[1], sys.argv[2], sys.argv[3])}")
"""Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text. Продолжить работу над заданием.
В программу должна попадать строка из слов, разделенных пробелом.
Каждое слово состоит из латинских букв в нижнем регистре.
Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
Необходимо использовать написанную ранее функцию int_func(). """
def int_func(text:str):
    return text.capitalize()
word_list = input("Ввкдите слова из маленьких латинских букв через пробел:\n").split()
for word in word_list:
    print(int_func(word), end=" ")
"""Программа запрашивает у пользователя строку чисел, разделенных пробелом.
При нажатии Enter должна выводиться сумма чисел.
Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы завершается.
Если специальный символ введен после нескольких чисел,
то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу."""
def sum_func(total=0):
    numbers = []
    user_input = input('Введите несколько чисел через пробел: ')
    user_list = user_input.split()
    if user_list[-1] == "/":
        for num in user_list[:-1]:
            numbers.append(int(num))
        total = total + sum(numbers)
        return total
    else:
        for num in user_list:
            numbers.append(int(num))
        total += sum(numbers)
        return sum_func(total)
print(sum_func())
"""Программа принимает действительное положительное число x и целое отрицательное число y.
Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной функции возведения числа в степень."""
def my_func(x: int, y: int):
    powered = x
    if x <= 0 or y >= 0:
        print("Неверный формат")
    else:
        for i in range(1, y, -1):
            powered /= x
    return powered
"""Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов."""
def my_func(num1, num2, num3):
    num_list = [num1, num2, num3]
    num_list.remove(min(num_list))
    return sum(num_list)
"""Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
Каждый кортеж хранит информацию об отдельном товаре.
В кортеже должно быть два элемента — номер товара и словарь с параметрами
(характеристиками товара: название, цена, количество, единица измерения).
Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара,
например название, а значение — список значений-характеристик, например список названий товаров."""
products_structure = {"название": str, "цена": int, "количество": int, "ед": str}
product_list = []
decision = "да"
products_count = 1
while decision == "да":
    products_info = {}
    for product_key, info_type in products_structure.items():
        products_info[product_key] = info_type(input(f"Введите значение '{product_key}': "))
    product_list.append((products_count, products_info))
    decision = input("Добавить другой товар? (Введите да или нет): ").lower()
    products_count += 1
print(product_list)
product_analysis = {}
for analytic_keys in products_structure.keys():
    item_list = []
    for product in product_list:
        item_list.append(product[1][analytic_keys])
        product_analysis[analytic_keys] = item_list
print(product_analysis)
"""Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
 У пользователя необходимо запрашивать новый элемент рейтинга.
Если в рейтинге существуют элементы с одинаковыми значениями,
то новый элемент с тем же значением должен разместиться после них."""
my_list = [7, 5, 3, 3, 2]
user_number = int(input('Введите число: '))
number_count = my_list.count(user_number)
if number_count:
    last_current_index = my_list.index(user_number) + number_count
    my_list.insert(last_current_index, user_number)
elif user_number > my_list[0]:
    my_list.insert(0, user_number)
elif user_number < my_list[-1]:
    my_list.append(user_number)
else:
    for idx, num in enumerate(my_list):
        if user_number > num:
            my_list.insert(idx, user_number)
            break
print(my_list)
"""Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки.
Строки необходимо пронумеровать. Если слово длинное, выводить только первые 10 букв в слове."""
words = input("Введите несколько слов через пробел: ").split()
for idx, word in enumerate(words, start=1):
    print(f"{idx}. {word:.10}")
"""Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень). Напишите решения через list и через dict."""
month_number = int(input("Введите номер месяца: "))
months = ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь",
          "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"]
season_dict = {(12, 1, 2): "Зима", (3, 4, 5): "Весна", (6, 7, 8): "Лето", (9, 10, 11): "Осень"}
season = None
for key in season_dict.keys():
    if month_number in key:
        season = season_dict[key]
        break
print(f"Сезон: {season} Месяц: {months[month_number-1]}")
"""Для списка реализовать обмен значений соседних элементов, т.е.
Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте."""
items = [2, 2, 5, 12, 8, 2, 25, -1, -5, -10, -15, -99, 105]
print(items)
i = 1
for idx in range(0, len(items) - 1, 2):
    next_idx = idx+1
    items[idx], items[next_idx] = items[next_idx], items[idx]
print(items)
"""Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров.
Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
Требуется определить номер дня, на который результат спортсмена составит не менее b километров.
Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.
Например: a = 2, b = 3.
Ответ: на 6-й день спортсмен достиг результата — не менее 3 км."""
start = int(input('Введите результат в первый день: '))
goal = int(input('Введите целевое значение: '))
day_result = start
day_counter = 1
while day_result < goal:
    day_counter += 1
    day_result *= 1.1
else:
    print(f'Ответ: на {day_counter}-й день спортсмен достиг результата — не менее {goal} км.')
"""Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает фирма
(прибыль — выручка больше издержек, или убыток — издержки больше выручки). Выведите соответствующее сообщение.
Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника."""
revenue = int(input('Введите сумму выручки: '))
costs = int(input('Введите сумму издержек: '))
profit = revenue - costs
if profit > 0:
    print(f'Прибыль {profit}')
    profitability = profit / revenue * 100
    print(f'Рентабельность выручки {profitability}%')
    workers_count = int(input('Введите численность сотрудников: '))
    print('Прибыль фирмы в расчете на одного сотрудника: ', profit / workers_count)
else:
    print(f'Убыток{profit}')
"""Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции."""
user_input = input('Введите число: ')
if not user_input.isdigit():
    print('Неверный формат числа')
    exit()
max_num = 0
number = int(user_input)
while number and max_num != 9:
    current = number % 10
    number //= 10
    max_num = current if current > max_num else max_num
print('Самая большая цифра в числе: ', max_num)
"""Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369."""
user_input = input('Введите число: ')
if not user_input.isdigit():
    print('Неверный формат числа')
    exit()
characters_count = 0
user_number = int(user_input)
temp_number = user_number
while temp_number:
    temp_number //= 10
    characters_count += 1
first_level_multiplication = 10 ** characters_count + 1
second_level_multiplication = 10 ** (characters_count * 2) + first_level_multiplication
result = user_number + user_number * first_level_multiplication + user_number * second_level_multiplication
print(result)
"""Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк."""
secs = input('Введите количество секунд: ')
if not secs.isdigit():
    print('Неверный формат числа')
    exit()
secs = int(secs)
hours, minutes, seconds = secs // 60 ** 2, (secs % 60 ** 2) // 60, secs % 60
print(f'{hours:>02}:{minutes:>02}:{seconds:>02}')