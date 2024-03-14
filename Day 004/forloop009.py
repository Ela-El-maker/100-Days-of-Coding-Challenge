gaming = {
    '11B': [362.5, 'PLN'],
    'CDR': [74.25, 'USD'],
    'CIG': [0.85, 'PLN'],
    'PLW': [79.5, 'USD'],
    'TEN': [300.0, 'PLN']
}

USDPLN = 4.0

for company, info in gaming.items():
    if info[1] == 'USD':
        info[0] *= USDPLN  # Convert USD to PLN
        info[1] = 'PLN'  # Update currency to PLN
    else:
        continue  # Skip if currency is already PLN

print(gaming)
