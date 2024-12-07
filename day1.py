with open("day1.txt") as reader:
    lines = reader.read().strip().split("\n")

l1 = [int(l.split(" ")[0]) for l in lines]
l2 = [int(l.split(" ")[-1]) for l in lines]

l1.sort()
l2.sort()

res1 = sum(abs(x-y) for x,y in zip(l1,l2))
print("Solution partie 1 = ",res1)

md = {x : l2.count(x) for x in l1}
res2 = 0
for x in md:
    res2 += x*md[x]

print("Solution partie 2 = ",res2)
