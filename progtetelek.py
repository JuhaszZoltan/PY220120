# egyszerű prog tetelek
# INPUT: sorozat
# OUTPUT: egy <valamilyen> érték

# [számláló ciklussal megvalósítható]
# sorozatszámítás (pl.: összegzés)
# megszámlálás
# szélsőérték meghatározás (minimum, maximum)

# [feltételes ciklussal megvalósítható]
# kiválasztás
# eldöntés
# lineáris keresés

sorozat = [26, 11, 23, 7, 69, 4, 15]
print(f'sorozat elemei: {sorozat}')

#sorozatszámítás: sorozat elemeinek összege
sum = 0
for elem in sorozat:
    sum += elem
print(f'sorozat elemeinek összege: {sum}')

# sorozat elemeinek átlaga
# (kell hozzá az összeg)
print(f'sorozat elemeinek átlaga: {sum/len(sorozat)}')

# sorozatszámítás: sorozat elemeinek szorzata
multi = 1
for elem in sorozat:
    multi *= elem
print(f'sorozat elemeinek szorzata: {multi}')

szavak = ['Alma', ' ', 'a', ' ', 'fa', ' ', 'alatt', '.']
mondat = '\0'
for szo in szavak:
    mondat += szo
print(f'az egész mondat: {mondat}')

# megszámlálás
count = 0
# tulajdonság: páros
for elem in sorozat:
    if elem % 2 == 0:
        count += 1
print(f'páros elemek száma a sorozatban: {count} db')

# szélsőérték meghatározás tétele: maximum meghatározás:

max_index = 0
for index in range(1, len(sorozat)):
    if sorozat[index] > sorozat[max_index]:
        max_index = index
print(f'a sorozat legnagyobb elemének indexe: {max_index}')
print(f'a sorozat legnagyobb eleme: {sorozat[max_index]}')
# minimum value/index meghatározásánál a feltételben a reláció iránya változik

### ------------------------------- ###

# kiválasztás - CSAK AKKOR alkalmazható, HA BIZTOSAN TUDHATÓ, hogy az elem BENNE VAN az adatszerkezetben

i = 0
keresett_elem = 69
while sorozat[i] != keresett_elem:
    i += 1
print(f'a {keresett_elem} indexe a(z) {i}.')

# eldöntés - van-e adott tulajdonságnak megfelelő elem a sorozatban
# pl.: van-e a sorozatban páros szám:
i = 0

#                          a teljesülési feltétel ELLENTETTJE
while i < len(sorozat) and sorozat[i] % 2 != 0:
    i += 1    
megfelel = i < len(sorozat)

if megfelel: print('van benne páros elem')
else: print('nincs benne páros elem')

# lineáris keresés (linker):
# van-e a sorozatban adott tulajdonságú elem? - és ha igen, akkor melyik az/hol van?
# pl.: van-e a sorozatban 3 többszöröse, és ha igen, akkor hol?

# sorozat = [10, 10, 10, 3, 10, 10, 10]
i = 0
#                          a teljesülési feltétel TAGADÁSA
while i < len(sorozat) and not (sorozat[i] != 3 and sorozat[i] % 3 == 0):
    i += 1

if i < len(sorozat):
    print(f'van benne 3 többszöröse, ez pedig a {sorozat[i]}, ami a sorozat {i} indexű eleme.')
else: print('nincs a sorozatban olyan szám, ami 3 többszöröse')