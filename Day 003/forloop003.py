probabilities = [0.21, 0.91, 0.34, 0.55, 0.76, 0.02]
probabs=[]

for probability in probabilities:
    if probability >=0.5:
        probabs.append(probability)
print(probabs)