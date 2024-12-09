import re

with open("day3.txt") as reader:
    content = reader.read().strip()

cpos = 0
res = 0
do = True
while cpos<len(content):
    if content[cpos:].startswith("mul(") and do:
        args =content[cpos+4:content.find(")",cpos)].split(',')
        try:
            res += int(args[0])*int(args[1])
        except:
            pass
    elif content[cpos:].startswith("do()"):
        do = True
    elif content[cpos:].startswith("don't()"):
        do = False
    cpos += 1

print(f"Solution partie 2 = {res}")