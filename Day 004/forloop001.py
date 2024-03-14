items = ['x', 'y', 'z', 'y', 'x', 'y', 'y', 'z', 'x']

counts = {}
for item in items:
    if item in counts:
        counts[item]+=1
    else:
        counts[item] = 1
        
    
print(counts)
    