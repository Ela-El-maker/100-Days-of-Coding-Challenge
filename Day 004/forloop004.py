gaming = {
    '11B': 362.5,
    'CDR': 297.0,
    'CIG': 0.85,
    'PLW': 318.0,
    'TEN': 300.0
}

for game,value in gaming.items():
    if value > 100.00 :
        print(game)