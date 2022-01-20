# eldöntés 'python spec cc'

sorozat = [26, 11, 23, 69, 7, 4, 15]

keresett = 69

for elem in sorozat:
    if elem == keresett:
        print(f'benne van a {keresett}')
        break
else: print(f'nincs benne a {keresett}')

# BÁRMILYEN ciklus 'else ága' akkor fut le, ha a ciklus iterációi alatt sosem futott le break

# linker whileal
i = 0
while i < len(sorozat):
    if sorozat[i] == keresett:
        print(f'a {keresett} a sorozat {i} indexű eleme')
        break
    i += 1
else: print(f'a {keresett} nincs benne a sorozatba')

# linker forral by Imola
for index in range(len(sorozat)):
    if sorozat[index] == keresett:
        print(f'a {keresett} a sorozat {index} indexű eleme')
        break
else: print(f'a {keresett} nincs benne a sorozatba')