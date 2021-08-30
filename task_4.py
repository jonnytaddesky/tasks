dict_1 = {'a': 1, 'b': 4}
dict_2 = {'c': 10, 'd': 11}
dict_3 = {'e': 14, 'f': 18}

result = {}

for i in (dict_1, dict_2, dict_3):
    result.update(i) 

print(result)