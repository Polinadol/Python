#1. Создать программный файл в текстовом формате, записать в него построчно данные,
# вводимые пользователем. Об окончании ввода данных будет свидетельствовать пустая строка.


#func = open('my_text.txt', 'w')
#stroka = input('Введите текст \n')
#while stroka:
#    func.writelines(stroka)
#    stroka = input('Введите текст \n')
#    if not stroka:
#        break
#print (stroka)
#func.close()

#2. Создать текстовый файл (не программно),
# сохранить в нём несколько строк, выполнить подсчёт строк и слов в каждой строке.

#file=open('test.txt','a')
#content =file.write(' \nI\n know\n who\n you\n are')
#file=open('test.txt','r')
#lines=0
#words=0
#for line in file:
#    lines +=1
#    words += len(line.split())

#print(lines)
#print(words)

#3. Создать текстовый файл (не программно).
# Построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
# Определить, кто из сотрудников имеет оклад менее 20 тысяч,
# вывести фамилии этих сотрудников. Выполнить подсчёт средней величины дохода сотрудников.

#tabel= open('tabel.txt', 'w')
#info=tabel.write( ' Ivanov 18000 \n Petrov 30000 \n Semenov 25000 \n Lopuhov 12000  \n Indukov 22000 \n Laptin 19000' )
#print(info)
#with open('tabel.txt', 'r') as tabel:
#    salary =[]
#    mini=[]
#    info=tabel.read().split('\n')
#    for i in info:
#       i=i.split()
#       if int(i[1]) <20000:
#           salary.append(i[0])
#       mini.append(i[1])

#print(f'Самый маленький оклад у:    {salary}, среднее арифметическое:{sum(map(int,mini))/len(mini)}  ')

#4. Создать (не программно) текстовый файл со следующим содержимым:
#One — 1
#Two — 2
#Three — 3
#Four — 4
#Напишите программу, открывающую файл на чтение и считывающую построчно данные.
#При этом английские числительные должны заменяться на русские.
#Новый блок строк должен записываться в новый текстовый файл

#dict={'One':'Один','Two':'Два','Three':'Три','Four':'Четыре'}
#rus_massiv=[]
#with open('zada4a 4.txt','r') as massiv:
#    new_massiv=massiv.read().split('\n')
#    for i in new_massiv:
#        i=i.split(' ',1)
#        rus_massiv.append((i[0])+ ' '+ i[1])
#print(rus_massiv)

#5. Создать (программно) текстовый файл, записать в него программно набор чисел,
# разделённых пробелами. Программа должна подсчитывать сумму чисел в файле и выводить её на экран.


#with open('zada4a 5.txt','w+') as spisok:
#    stroka=(input('Введите числа через пробел:  '))
#    spisok.writelines(stroka)
#    cifry=stroka.split()

#    print('Сумма чисел равна:  ',sum(map(int,cifry)))

#6. Сформировать (не программно) текстовый файл. В нём каждая строка должна описывать
# учебный предмет и наличие лекционных, практических и лабораторных занятий по предмету.
# Сюда должно входить и количество занятий. Необязательно, чтобы для каждого предмета
# были все типы занятий.Сформировать словарь, содержащий название предмета и
# общее количество занятий по нему. Вывести его на экран.

#import json
#dict={}
#with open('zada4a 6','r', encoding='utf-8') as file:
#    print(file.read())
#    for line in file:
#        urok, lekcia,laba,praktika=line.split()
#        dict[urok]=int(lekcia)+int(laba)+int(praktika) # Не могу понять, почему здесь не разделяется?
#    print(f'{dict}')

# Создать вручную и заполнить несколькими строками текстовый файл,
#    в котором каждая строка должна содержать данные о фирме:
#    название, форма собственности, выручка, издержки.
#    Пример строки файла: firm_1   ООО   10000   5000.
#    Необходимо построчно прочитать файл, вычислить прибыль каждой
#    компании, а также среднюю прибыль. Если фирма получила убытки,
#    в расчет средней прибыли ее не включать.
#    Далее реализовать список. Он должен содержать словарь
#    с фирмами и их прибылями, а также словарь со средней прибылью.
#    Если фирма получила убытки, также добавить ее в словарь
#    (со значением убытков).
#    Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000},
#    {“average_profit”: 2000}].
#    файл.
#    Пример json-объекта:
#    [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000},
#    {"average_profit": 2000}]
#Подсказка: использовать менеджер контекста.
#import json
#profit = {}
#pr = {}
#prof = 0
#prof_aver = 0
#i = 0
#with open('zada4a 7.txt', 'r') as file:
 #   for line in file:
 #       name, form, earning, expense = line.split()
#        profit[name] = int(earning) - int(expense)
#        if profit.setdefault(name) >= 0:
 #           prof = prof + profit.setdefault(name)
#            i += 1
#    if i != 0:
#        prof_aver = prof / i
#        print(f'Прибыль средняя - {prof_aver:.2f}')
#    else:
#        print(f'Прибыли нет')
#    pr = {'средняя прибыль': round(prof_aver)}
#    profit.update(pr)
#    print(f'Прибыль  - {profit}')
#
#with open('zada4a 7.json', 'w') as write_js:
#    json.dump(profit, write_js)

#    js_str = json.dumps(profit)
#    print(f' файл  json : \n '
#          f' {js_str}')

