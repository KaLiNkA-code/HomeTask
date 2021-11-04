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
