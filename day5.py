from functools import cmp_to_key

with open("day5.txt") as reader:
    rules, updates = reader.read().strip().split('\n\n')

rules = rules.split('\n')
rules = [tuple(map(int,r.split('|'))) for r in rules]

updates = updates.split('\n')
updates = [tuple(map(int,u.split(','))) for u in updates]
         

before = {}
for previous, next in rules:
    if next not in before:
        before[next]=[]
    if previous not in before:
        before[previous]=[]
    before[next].append(previous)

res1 = 0
to_reorder = []
for u in updates:
    if all(u[i] in before for i in range(1,len(u))):
        if all(u[i-1] in before[u[i]] for i in range(1,len(u))):
            res1 += u[len(u)//2]
        else:
            to_reorder.append(list(u))
    else:
        to_reorder.append(list(u))
    
print(f"Réponse partie 1 = {res1}")


def cmp_before(x,y):
    if x in before[y]:
       return -1
    return 1 

res2 = 0
for r in to_reorder:
    r.sort(key=cmp_to_key(cmp_before))
    res2 += r[len(r)//2]


print(f"Réponse partie 2 = {res2}")
