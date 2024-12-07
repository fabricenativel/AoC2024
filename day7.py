with open("day7.txt") as reader:
    content = reader.read().strip().split('\n')

content = [c.split(":") for c in content]
results = [int(r[0]) for r in content]
operands = [tuple(map(int,r[1].strip().split(" "))) for r in content]


def to_base3(n):
    if n==0: return "0"
    res = ""
    while n!=0:
        res = str(n%3) + res
        n = n//3
    return res

def op(x,y,op):
    if op=="2":
        return int(str(x)+str(y))
    return x+y if op=="1" else x*y

def compute(operands, operations):
    assert len(operations) == len(operands) -1
    res = op(operands[0],operands[1],operations[0])
    for i in range(1,len(operations)):
        res = op(res, operands[i+1],operations[i])
    return res

def check(result, operands):
    operations = 0
    size = len(operands)-1
    while operations<=2**(size)-1:
        to_do = bin(operations)[2:].zfill(size)
        if compute(operands,to_do)==result:
            return True,result
        operations +=1
    return False, 0


def check3(result, operands):
    operations = 0
    size = len(operands)-1
    while operations<3**size:
        to_do = str(to_base3(operations)).zfill(size)
        if compute(operands,to_do)==result:
            return True,result
        operations +=1
    return False, 0

values = [check(res, oper) for (res,oper) in zip(results, operands)]
p1 = sum([v[1] for v in values])
print(f"Résultat partie 1 = {p1}")

values = [check3(res, oper) for (res,oper) in zip(results, operands)]
p2 = sum([v[1] for v in values])
print(f"Résultat partie 1 = {p2}")