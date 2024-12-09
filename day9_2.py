with open("day9.txt") as reader:
    data = list(map(int,reader.read().strip()))

diskmap = []
fid = 0
fsize = {}
fstart = {}
for i in range(len(data)):
    if i%2==0:
        diskmap = diskmap+ [str(fid)]*data[i]
        fsize[fid]=data[i]
        fstart[fid] = len(diskmap)-data[i]
        fid += 1
    else:
        diskmap = diskmap + ['.']*data[i]


def find_start(diskmap,s,mi):
    for i in range(mi):
        if diskmap[i:i+s]==["."]*s:
            return i
    return -1

for i in range(fid-1,-1,-1):
    p = find_start(diskmap,fsize[i],fstart[i]) 
    if p!=-1:
        for j in range(fsize[i]):
            diskmap[p+j],diskmap[fstart[i]+j] = diskmap[fstart[i]+j],diskmap[p+j]

res = 0
for i in range(len(diskmap)):
    if diskmap[i]!='.':
        res += i*int(diskmap[i])

print(f"Partie 2 = {res}")