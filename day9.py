with open("day9.txt") as reader:
    data = list(map(int,reader.read().strip()))

diskmap = []
fid = 0
for i in range(len(data)):
    if i%2==0:
        diskmap = diskmap+ [str(fid)]*data[i]
        fid += 1
    else:
        diskmap = diskmap + ['.']*data[i]

cpos = len(diskmap)-1

while "." in diskmap[:cpos+1]:
    freepos = diskmap[:cpos+1].index(".")
    diskmap[cpos], diskmap[freepos] = diskmap[freepos], diskmap[cpos]
    cpos -= 1

res = 0
for i in range(cpos+1):
    res += i*int(diskmap[i])

print(f"Partie 1 = {res}")