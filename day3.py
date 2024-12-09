import re

with open("day3.txt") as reader:
    content = reader.read().strip()

res =  re.findall(r'mul\(\d+,\d+\)',content)

res2 = re.findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)",content)
print(res2)
p1 = 0
for m in res:
    n1,n2 = tuple(map(int,re.findall(r'\d+',m)))
    p1 += n1*n2

do = True

p2=0
for m in res2:
    if m=="do()":
        do = True
    elif m=="don't()":
        do = False
    else:
        if do:
            n1,n2 = tuple(map(int,re.findall(r'\d+',m)))   
            p2 += n1*n2


print(f"Solution partie 1 = {p1}")
print(f"Solution partie 1 = {p2}")

