result = []

for i in range(1, 100):
    if i % 11 == 0 and i % 3 != 0:
        result.append(str(i))

print(','.join(result))
