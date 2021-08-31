string_number = input('Введите числа через запятую: ')

print(list(map(int, string_number.split(','))))
print(tuple(map(int, string_number.split(','))))
