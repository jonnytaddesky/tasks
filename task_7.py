def pascal_triangle(n):
    row = [1]
    y = [0]
    for x in range(max(n, 0)):
        print(row)
        ar = []
        for left, right in zip(row + y, y + row):
            ar.append(left + right)
        row = ar


pascal_triangle(6)
