with open("06_big_1.txt") as reader:
    grid = reader.read().strip().split('\n')

DIR = {"^":(-1,0),"v":(1,0),">":(0,1),"<":(0,-1)}
TURN = {(-1,0):(0,1), (1,0):(0,-1), (0,1):(1,0), (0,-1):(-1,0)}
SYMB = {(-1,0):"^",(1,0):"v",(0,1):">",(0,-1):"<"}
nbl,nbc = len(grid), len(grid[0])
for l in range(nbl):
    for c in range(nbc):
        if grid[l][c] in "^>v<":
            sgl, sgc = l,c
            gl, gc = l,c
            gdl, gdc = DIR[grid[l][c]]
            sgdl, sgdc = gdl, gdc
            grid[l] = grid[l].replace(grid[l][c],".")

def in_map(l,c):
    return 0<=l<nbl and 0<=c<nbc

def view_map(gl,gc,gdl,gdc):
    for l in range(nbl):
        if l!=gl:
            print(grid[l])
        else:
            print(grid[l][:gc]+SYMB[(gdl,gdc)]+grid[l][gc+1:])

seen = set()
seen.add((gl,gc))
while in_map(gl+gdl,gc+gdc):
    if grid[gl+gdl][gc+gdc]=='.':
        gl += gdl
        gc += gdc
        if (gl,gc) not in seen:
            seen.add((gl,gc))
    else:
        gdl,gdc = TURN[(gdl,gdc)]
    
print(f"Réponse partie 1 = {len(seen)}")


nb_loop = 0
for (l,c) in seen:
    if (l,c)!=(sgl,sgc) and grid[l][c]=='.':
        ngrid = grid[:]
        ngrid[l]=ngrid[l][:c]+"#"+ngrid[l][c+1:]
        loop = False
        visited = set()
        visited.add((sgl,sgc,sgdl,sgdc))
        gl, gc, gdl, gdc = sgl, sgc, sgdl, sgdc
        while in_map(gl+gdl,gc+gdc) and not loop:
            if ngrid[gl+gdl][gc+gdc]=='.':
                gl += gdl
                gc += gdc
            else:
                gdl,gdc = TURN[(gdl,gdc)]
            if (gl,gc,gdl,gdc) not in visited:
                visited.add((gl,gc,gdl,gdc))
            else:
                loop=True
        if loop:
            nb_loop += 1

print(f"Réponse partie 2 : {nb_loop}")
