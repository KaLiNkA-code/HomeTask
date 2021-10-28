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

