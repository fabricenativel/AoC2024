with open("day2.txt") as reader:
    content = reader.read().strip().split('\n')

reports = [list(map(int,l.split(' '))) for l in content]

def is_safe(report):
    return all(0<report[i+1]-report[i]<4 for i in range(len(report)-1)) or all(0<report[i]-report[i+1]<4 for i in range(len(report)-1))

def one_error(report):
    for i in range(len(report)):
        nr = report[:i]+report[i+1:]
        if is_safe(nr):
            return True


print(f"Résultat partie 1 = ",[is_safe(r)  for r in reports].count(True))
print(f"Résultat partie 2 = ",[is_safe(r) or one_error(r) for r in reports].count(True))