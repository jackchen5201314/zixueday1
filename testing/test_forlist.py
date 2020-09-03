b = []
a = [-10, -3, -2, -1, 0, 1, 2, 3, 4, 6]
for i in a:
    for j in a:
        if i + j == 0:
            b.append([i, j])

print(b)
