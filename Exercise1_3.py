#alphabet_list = ['а','б','в','г','д','е','ё','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш','щ','ъ','ы','ь','э','ю','я']
#new_list = []
#for i in range(0,33):
#    new_list += alphabet_list[i].upper()
#    print(new_list)


#Задание 1.3.1
a = ord('а')
alphabet_list = []
for i in range(a,a+32):
    alphabet_list += ''.join([chr(i)]).upper()
    print(alphabet_list)



#Задание 1.3.2
import random
user_n = int(input('Введите количество строк n: '))
user_m = int(input('Введите рколичество столбцов m: '))
numb_list = []
for n in range(user_n):
    numb_list.append([])
    for m in range(user_m):
        numb_list[n].append(random.randint(1,100))
print(numb_list)

#for i in range(user_n):
#    numb_list.append([0]*user_m)
#    for j in range(user_m):
#         numb_list[i][j] = random.randint(1,100)
#print(numb_list)



#Задание 1.3.3
vertex_list = [[]]
def triang_area(vertex_list):
    x = []
    y = []
    for i in vertex_list:
        x.append(i[0])
        y.append(i[1])
    #print(x)
    #print(y)
 
    reskx = x[0] * y[1] + x[1] * y[2] + x[2] * y[3] + x[3] * y[4] + x[4] * y[0]
    resky = x[1] * y[0] + x[2] * y[1] + x[3] * y[2] + x[4] * y[3] + x[0] * y[4]
    resxy = abs(reskx - resky)/2
    print(resxy)    

vertex_list = [[0 for i in range(2)] for j in range(5)]
for i in range(5):
    for j in range(2):
        vertex_list[i][j] = float(input(f'Введите координаты {i+1} точки: '))
    print(vertex_list)

Square = triang_area(vertex_list)


#Задание 1.3.4
user_roman = input('Введите римское число: ')

def from_roman(num):
    roman_numerals = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    result = 0
    for i,c in enumerate(num):
        if (i+1) == len(num) or roman_numerals[c] > roman_numerals[num[i+1]]:
            result += roman_numerals[c]
        else:
            result -= roman_numerals[c]
    print(result)
arab_num = from_roman(user_roman)


#Задание 1.3.5
numberof_throw = int(input('Введите количетсво бросков: '))
numb ={2:0, 3:0, 4:0, 5:0, 6:0, 7:0,8 :0, 9:0, 10:0, 11:0, 12:0}
for i in range(numberof_throw):    
    cub1 = random.randint(1,6)
    cub2 = random.randint(1,6)
    points = cub1 + cub2
    numb[points] += 1    
print(numb)

