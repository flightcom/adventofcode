dico = {0: 10, 1: 2, 2: 5}

keys = list(dico.keys())
print(keys)
values = list(dico.values())
print(values)
# dico.pop(1)
# print(dico)

# dico = {x: y for x, y in dico.items()}
# liste = {i: y for i, x, y in enumerate(dico.items())}
# liste = {i: y for i, (x, y) in enumerate(dico.items())}
# print(liste)
# print(list(dico.keys()))
keys = [x if x < 2 else (x+1) for x in keys]
# print(liste)

keys.insert(2, 2)
print(keys)
values.insert(2, 99)
print(values)

dico = dict(zip(keys, values))

# dico = {(x if x < 2 else (x+1)): y for x, y in dico.items()}
print(dico)
