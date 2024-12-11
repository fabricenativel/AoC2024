with open("day10.txt") as reader:
    content = reader.read().strip().split('\n')

grid = [list(map(int,list(l))) for l in content]
ADJ = [(0,1),(0,-1),(1,0),(-1,0)]

def in_grid(l,c):
    return 0<=l<len(grid) and 0<=c<len(grid[0])

def count_path(l,c):
    if grid[l][c]==0:
        return 1
    return sum([count_path(l+dl,c+dc) for (dl,dc) in ADJ if in_grid(l+dl,c+dc) and grid[l+dl][c+dc]==grid[l][c]-1])

print(f"Partie 2 = {sum([count_path(l,c) for l in range(len(grid)) for c in range(len(grid[0])) if grid[l][c]==9])}")