from itertools import combinations

pokedex = {
    "Pikachu": ("Electric",),
    "Charizard": ("Fire", "Flying"),
    "Lapras": ("Water", "Ice"),
    "Machamp": ("Fighting",),
    "Mewtwo": ("Psychic", "Fighting"),
    "Hoopa": ("Psychic", "Ghost", "Dark"),
    "Lugia": ("Psychic", "Flying", "Water"),
    "Squirtle": ("Water",),
    "Gengar": ("Ghost", "Poison"),
    "Onix": ("Rock", "Ground")
}

bestteam = None
besttypes = set()

for team in combinations(pokedex.keys(), 3):  
    combinedset = set()
    for p in team:
        combinedset.update(pokedex[p])  

    if len(combinedset) > len(besttypes):
        bestteam = team
        besttypes = combinedset

print("Best Team:", bestteam)
print("Types Covered:", besttypes)
print("Strength:", len(besttypes))
