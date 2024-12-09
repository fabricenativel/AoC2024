with open("day4.txt") as reader:
    lines = reader.read().strip().split('\n')

WORD = "XMAS"
DIR = [(i,j)  for i in range(-1,2) for j in range(-1,2) if (i,j) != (0,0)]


nb = 0
for i in range(len(lines)):
    for j in range(len(lines[0])):
        if lines[i][j]=="X":
                for dx,dy in DIR:
                    m = "X"
                    if 0<=i+dx*3<len(lines) and 0<=j+dy*3<len(lines):
                        for k in range(1,4):
                            m = m + lines[i+dx*k][j+dy*k]
                        if m==WORD:
                             nb+=1

print(f"Partie 1 = {nb}")

nb2 = 0
for i in range(len(lines)-2):
     for j in range(len(lines[0])-2):
          if    (lines[i][j]=="M" and lines[i+1][j+1]=="A" and lines[i+2][j+2]=="S" and lines[i][j+2]=="M" and lines[i+2][j]=="S") or  (lines[i][j]=="S" and lines[i+1][j+1]=="A" and lines[i+2][j+2]=="M" and lines[i][j+2]=="S" and lines[i+2][j]=="M") or (lines[i][j]=="M" and lines[i+1][j+1]=="A" and lines[i+2][j+2]=="S" and lines[i][j+2]=="S" and lines[i+2][j]=="M") or ((lines[i][j]=="S" and lines[i+1][j+1]=="A" and lines[i+2][j+2]=="M" and lines[i][j+2]=="M" and lines[i+2][j]=="S") ) :
               nb2+=1

print(f"Partie 2 = {nb2}")