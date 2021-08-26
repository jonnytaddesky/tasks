import operator
d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}

sorted_values = sorted(d.values())
sorted_dict = {}


for i in sorted_values:
    for k in d.keys():
        if d[k] == i:
            sorted_dict[k] = d[k]
            break
print(sorted_dict)
