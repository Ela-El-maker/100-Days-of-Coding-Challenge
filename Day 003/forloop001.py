items = [1, 5, 3, 2, 2, 4, 2, 4]

res = []
for i in items:
    if i not in res:
        res.append(i)
        
print(res)