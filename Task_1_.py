'''
Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
Пользователь в первой строке вводит натуральное число N –
количество элементов в массиве. В последующих  строках записаны
N целых чисел Ai. Последняя строка содержит число X
'''
from random import randint

N = int(input("Введите размер массива: "))
X = int(input("Введите искомое число: "))
count = 0
my_list = [randint(0,10) for _ in range(N)]
print(my_list)
for _ in my_list:
    if _ == X:
        count+=1
print(count)



