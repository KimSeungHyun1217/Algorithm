from collections import deque

def solution(maps):
    answer = 0
    lenx , leny =  len(maps) , len(maps[0])
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    check = []
    queue = deque()
    queue.append([0,0])

    
    while queue:
        x,y = queue.popleft()
        
        for i in range(4):
            tx = x+dx[i]
            ty = y+dy[i]
            if tx >= 0 and tx <lenx and ty >=0 and ty <leny:
                if maps[tx][ty] == 1 :
                    maps[tx][ty] = maps[x][y] + 1              
                    queue.append([tx,ty])
    answer = maps[lenx-1][leny-1] 
    return -1 if answer == 1 else answer
                        