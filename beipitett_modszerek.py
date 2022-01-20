sorozat = [26, 11, 23, 69, 7, 4, 15]
keresett = 69

# összegzés
elemek_osszege = sum(sorozat)
print(f"sum: {elemek_osszege}")

# minimum ÉRTÉK
legkisebb_elem = min(sorozat)
print(f'min: {legkisebb_elem}')

# maximum ÉRTÉK
legnagyobb_elem = max(sorozat)
print(f'max: {legnagyobb_elem}')

# tartalmaz-e? [azaz az eldöntés tételének leggyakoribb alkalmazása]
benne_van = keresett in sorozat
print(f"tartalmazza A {keresett}-ET: {benne_van}")

# adaott elem indexe [azaz kvázi kiválasztás]
# CSAK HA |||TUDOD|||, hogy benne van, mert így ha nincs benne, akkor összeomolna - tehát olyankor linker-t kell használni
index = sorozat.index(keresett)
print(f'a {keresett} indexe: {index}')

# lineáris keresés
if keresett in sorozat:
    index = sorozat.index(keresett)
    print(f'benne van, a {index} indexű elem')
else: print('nincs benne')

# max index:
maxi = sorozat.index(max(sorozat))
print(f'max index: {maxi}')

# min index:
mini = sorozat.index(min(sorozat))
print(f'min index: {mini}')

# hányszor van benne a 'keresett' elem (aka. megszámlálás egy spec. esete)
c = sorozat.count(keresett)
print(f'a {keresett} {c}-szer szerepel a sorozatban')