from heapq import nlargest, nsmallest
my_dict = {'a': 500, 'b': 5874, 'c': 560, 'd': 400, 'e': 5874, 'f': 20}

print(sorted(my_dict, key=my_dict.get, reverse=True)[:3])

print(nlargest(3, my_dict, key=my_dict.get))
print(nsmallest(3, my_dict, key=my_dict.get))
