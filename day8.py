from itertools import combinations

with open("day8.txt") as reader:
    grid = reader.read().strip().split('\n')

antennas = {}
nbl = len(grid)
nbc= len(grid[0])

def in_grid(z):
    return 0<=z.imag<nbl and 0<=z.real<nbc

def sym(z,c):
    return 2*c-z

def allsym(z,c):
    res = set()
    res.add(z)
    res.add(c)
    while in_grid(2*c-z):
        res.add(2*c-z)
        c,z = 2*c-z,c
    return res

for l in range(nbl):
    for c in range(nbc):
        if grid[l][c]!='.':
            if grid[l][c] in antennas:
                antennas[grid[l][c]].append(c+l*1j)
            else:
                antennas[grid[l][c]]= [(c+l*1j)]

antinodes1 = set()
antinodes2 = set()
for symb in antennas:
    for z1,z2 in combinations(antennas[symb],2):
        antinodes1.add(sym(z1,z2))
        antinodes1.add(sym(z2,z1))
        antinodes2 = antinodes2.union(allsym(z1,z2))
        antinodes2 = antinodes2.union(allsym(z2,z1))
        
print(f"Partie 1 = {len([z for z in antinodes1 if in_grid(z) and z not in antennas])}")
print(f"Partie 2 = {len(antinodes2)}")