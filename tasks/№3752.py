"""Во входной строке записана последовательность чисел через пробел.
Для каждого числа выведите слово YES (в отдельной строке),
если это число ранее встречалось в последовательности или NO,
если не встречалось."""
numbers = list(input('enter numbers: ').split())
new_numbers = set()
for i in numbers:
    if i not in new_numbers:
        print('NO')
        new_numbers.add(i)
    else: print('YES')

