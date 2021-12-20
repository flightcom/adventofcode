# l = [1, 2, 3, 4, 5]

# print(l[-2:])

# liste = [False, False, False]

# print(sum(liste))

# liste = [1, 2, 2, 2, 2, 3, 2, 4]

# print(min([i for i, n in enumerate(liste) if n != 2 and i > 1]))

# print(liste[3])


dico = {
    2: 30,
    4: 50,
    3: 10,
    10: 100
}

meta = [1, 2, 2, 5]
total = 0
# dico_filtered = {x: y for x, y in dico.items() if x > 0 and x < 5}
dico_filtered = [y for x, y in dico.items() if x > 0 and x < 5]
children_values = [dico_filtered[i-1] for i in meta if len(dico_filtered) > i]
total += sum(children_values)

print(total)
