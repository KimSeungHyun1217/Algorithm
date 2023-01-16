def big(a,b):
    if a>b:
        return a,b
    else:
        return b,a
def solution(dirs):
    check = []
    ax , ay = 0 , 0

    for i in dirs:
        if i == 'L':
            if ax-1 < -5: continue
            t1,t2 = big(ax-1,ax)
            if [t1,t2,ay,ay] not in check:
                check.append([t1,t2,ay,ay])
            ax -= 1
        elif i == 'R':
            if ax+1 > 5: continue
            t1,t2 = big(ax+1,ax)
            if [t1,t2,ay,ay] not in check:
                check.append([t1,t2,ay,ay])
            
            ax += 1
                  
        elif i == 'U':
            if ay+1 > 5: continue
            t1,t2 = big(ay,ay+1)
            if [ax,ax,t1,t2] not in check:
                check.append([ax,ax,t1,t2])
            
            ay += 1
        else:
            if ay-1 < -5: continue
            t1,t2 = big(ay-1,ay)
            if [ax,ax,t1,t2] not in check:
                check.append([ax,ax,t1,t2])
            
            ay -= 1
    return len(check)