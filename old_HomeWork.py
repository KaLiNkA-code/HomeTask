"""
Калинин Егор 9 класс
23.10.21
Ex 1
"""


massiv = []  # random int and len massiv
result_dict = {}
m = 0
r = None
for i in massiv:
    if i in result_dict:
        result_dict[i] += 1
    else:
        result_dict[i] = 1

for k, i in result_dict.items():
    if m < i:
        m = i
        r = k

print(r)  # O(N) (Линейная сложность алгоритма (вроде))


"""Ex 2"""
result = []
S = 'SSSJSSJSJJJSJSJSJSJJ'  # random str
J = 'SSSJJSJSJJSJSJSJSSJJ'  # random str
r1 = ''

for j in J:
    r1 += j  # Да, резы. Но другое в голову не приходет. Я вообще сомневаюсь, что я правильно задачу понял АХАХАХАХАХАХ
    if r1 in S:
        result.append(r1)
    else:
        r1 = ''
print(", ".join(result))
"""Ex 3"""


massiv = [8, 6, 6, 4, 3, 2, 2, 1]  # random int and len massiv
c = 0
result = []
for i in massiv:
    if i != c:
        c = i
        result.append(i)

print(result)  # O(N) (Получается тоже линейная сложность (вроде))

"""
Калинин Егор 9 класс
30.10.21
Ex 1
"""
num = 2
random_list = [1, 'Hi', True, ['My', 3], (1, num, 3, [4.3, 4.6], 5)]
"""Ex2"""

random_list.append('String')

"""Ex3"""

random_list[0] = 10

"""Ex4"""

rl = [9, 8, 76]
random_list.append(rl)

"""Ex5"""

random_tuple = ('Hash', 'Memory')
random_list[1] = random_tuple

"""Ex6"""

print(random_list[4])

"""Ex 7"""

del random_list[3]

"""Ex 8"""

list_input = input('list')
element_input = input('element')

"""Ex9 """

name = input()
print(f"Hello, {name}!")  # Python 3.7

"""Ex 10"""

answers = []
for _ in range(3):
    answers.append(input())

print(int(max(answers)) - int(min(answers)))


"""
Калинин Егор 9 класс
06.11.21
Ex 1 'сумма трех чисел'
"""

IntInput = [int(input()) for i in range(3)]
print(f"Сумма: {sum(IntInput)}")

"""Ex 2 'Следующее и предыдущее'"""

value = int(input("Введите число"))
print(f"предыдущие число: {value-1}\nследующее число: {value+1}")


"""Ex 3 'Трехзначное число'"""

value = input()
f, s, t = [int(i) for i in str(value)]
print(f"Сумма: {s+t+f}\nПроизведение: {f*s*t}")


"""Ex 4 'Элементы ряда Фибоначи'"""

count = 1
row = [1, 2]
result = 0
while row[count] + row[count-1] < 4_000_000:
    row.append(int(row[count] + row[count-1]))
    count += 1
    if row[count] % 2 == 0:
        result += row[count]

print(result)
print(row)
