#Упражнение 1.1.2

while(True):
    user_year = input('Введите год для проверки:')
    if (user_year == 'q'): break
    try:
        year = int(user_year)
    except ValueError:
        print('Некорректный ввод')
        continue
    if year % 4 == 0 or (year % 100 == 0 and year % 400 == 0) :
        print(f'{year} год високосный')
    else:
        print(f'{year} год невисокосный')
    user_cont = input('Хотите продолжить?Введите y(да) или n(нет) ')
    if user_cont == 'y':
        continue
    else: break
    

#Упражнение 1.1.3
    
while(True):
    user_name = input('Введите имя: ')
    user_sex = input('Введите пол: ')
    user_age = input('Введите возраст: ')    
    if (user_name == '1' or user_sex == '2' or user_age == 'r'): break
    try:        
        age = int(user_age)        
    except ValueError:
        print('Некорректный ввод')
        continue
    if user_sex == 'мужской' or user_sex == 'man':
        print(f'Его зовут {user_name}. Ему {age} лет.')
    else:
        print(f'Её зовут {user_name}. Ей {age} лет.')
    user_cont = input('Хотите продолжить?Введите y(да) или n(нет) ')
    if user_cont == 'y':
        continue
    else: break
    

#Упражнение 1.1.4
    
while(True):
    user_n = input('Рассчитать факториал числа: ')
    if (user_n == 'q'): break
    try:
        n = int(user_n)
    except ValueError:
        print('Некорректный ввод')
        continue
    i = 1
    fact = 1
    if n == 0 or n == 1:
        print(f'Факториал числа {n} равен {fact}')
    else:
        while i <= n:
            fact *= i
            i += 1
        print(f'Факториал числа {n} равен {fact}')
    user_cont = input('Хотите продолжить?Введите y(да) или n(нет) ')
    if user_cont == 'y':
        continue
    else: break
    

#Упражнение 1.1.5
    
"""for n in range(1000, 10000):
    num = n
    s = str(num)
    setarr = set(s)
    if len(s) == len(setarr):
        print(s)"""
        
            
        
#Упражнение 1.1.6
        
from math import sqrt

while(True):  
    
    user_n = input('Введите границу диапазона: ')
    if (user_n == 'q'):    break
    try:
        n = int(user_n)
    except ValueError:
        print('Некорректный ввод')
        continue
    #i, j = 2, 0
    for numb in range(1,n+1):
        k = 0
        for i in range(2, numb // 2+1):
            if numb % i == 0:
                k += 1
        if k <= 0:
            print(numb)        
    
    user_cont = input('Хотите продолжить?Введите y(да) или n(нет) ')
    if user_cont == 'y':
        continue
    else: break


#Упражнение 1.2.1    

while(True): 
    user_name = input('Введите вашу фамилию, имя и отчетсво: ')
    if (user_name == '1'): break
    try:
        full_name = str(user_name)
    except ValueError:
        print('Некорректный ввод')
        continue
    name_list = full_name.split()
    new_name = name_list[1][0].title() + '.'
    new_fathername = name_list[2][0].title() + '.'
    new_fullname = name_list[0].title() + ' ' + new_name +  new_fathername
    print(new_fullname)

    user_cont = input('Хотите продолжить?Введите y(да) или другую клавишу, если нет ')
    if user_cont == 'y':
        continue
    else: break




#Упражнение 1.2.2

user_string = input('Введите любую строку: ')
num_list = [] 
num = ''
summ = 0
for char in user_string:
    if char.isdigit():
        num = num + char
    else:
        if num != '':
            num_list.append(int(num))
            summ = summ + int(num)
            num = ''            
if num != '':
    num_list.append(int(num))
summ = summ + int(num)
 
print(num_list, f' summa = {summ}')
