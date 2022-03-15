import sys

input = sys.stdin.readline

dae=so=gong=num = 0



while True:
    word = input()[:-1]
    dae = so = gong = num = 0
    if not word:
        break
    for i in word:
        if i.isalpha():
            if ord(i) >=65 and ord(i)<=90:
                dae +=1
            else:
                so += 1
        elif ord(i)>=48 and ord(i)<=57:
            num += 1
        else:
            gong += 1
    print(so,dae,num,gong)

