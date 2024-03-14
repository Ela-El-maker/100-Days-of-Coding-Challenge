probabilities = [0.21, 0.91, 0.34, 0.55, 0.76, 0.02]
probability = []
for probabs in probabilities:
    if probabs < 0.5:
        probability.append(0)
    elif probabs >= 0.5:
        probability.append(1)
print(probability)