def d(a: list):
    re= []
    for i in a:
        b = i
        suma = i
        for j in range(len(str(i))):
            b = b + (suma % 10)
            suma = suma//10
        if b<=10000:
            re.append(b)
    return re

a = list(range(1,10001))
removea = list(set(d(a)))


for i in removea:
    x = i
    a.remove(x)

for i in a:
    print(i)



