a,b = map(int,input().split())
assert a>=b
def countnum(x,y):
    count = 0
    while x:
        x//=y
        count += x
    return count


fc = countnum(a,5) - countnum(b,5) - countnum(a-b,5)
tc = countnum(a,2) - countnum(b,2) - countnum(a-b,2)

print(min(fc,tc))