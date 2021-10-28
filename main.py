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
