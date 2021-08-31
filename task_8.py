string = 'abba'


def polindrom_1(string):
    return string == ''.join(reversed(string))


def polindrom_2(string):
    return string == string[::-1]


print(polindrom_1(string))

print(polindrom_2(string))
