d = []

for i in range(19):
    d.append([])
    for j in range(19):
        d[i].append(0)
        
for i in range(19):
    a = list(map(int, input().split()))
    for j in range(19):
        d[i][j] = a[j]
        
n = int(input())

for i in range(n):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    
    for i in range(19):
        if d[x][i] == 0:
            d[x][i] = 1
        else:
            d[x][i] = 0
    
    for i in range(19):
        if d[i][y] == 0:
            d[i][y] = 1
        else:
            d[i][y] = 0
            
for x in range(19):
    for y in range(19):
        print(d[x][y], end=' ')
    print()        