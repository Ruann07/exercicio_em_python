def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1



valores = [5, 7, 2, 11, 0, 5]
print(valores)
print('Dobrando...')
dobra(valores)
print(valores)

