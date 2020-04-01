def gen(i,j,c):
    return j+1+(i*c)

def cUp(m,i,j):
    return (m[i-1][j]!="#")
def cRight(m,i,j):
    return (m[i][j+1]!="#")
def cDown(m,i,j):
    return (m[i+1][j]!="#")
def cLeft(m,i,j):
    return (m[i][j-1]!="#")

def getAdjecencyList(m,r,c):
    g={}
    for i in range(0,r):
        for j in range(0,c):
            if m[i][j]!="#":
                en=gen(i,j,c)
                if en not in g:
                    g[en]=[]
                if i==0:
                    if cDown(m,i,j):
                            g[en].append(gen(i+1,j,c))
                    if j==0:
                        if cRight(m,i,j):
                            g[en].append(gen(i,j+1,c))                      
                    elif j==c-1:
                        if cLeft(m,i,j):
                            g[en].append(gen(i,j-1,c))
                    else:
                        if cRight(m,i,j):
                            g[en].append(gen(i,j+1,c))
                        if cLeft(m,i,j):
                            g[en].append(gen(i,j-1,c))  
                elif i==r-1:
                    if cUp(m,i,j):
                            g[en].append(gen(i-1,j,c))
                    if j==0:
                        if cRight(m,i,j):
                            g[en].append(gen(i,j+1,c))                      
                    elif j==c-1:
                        if cLeft(m,i,j):
                            g[en].append(gen(i,j-1,c))
                    else:
                        if cRight(m,i,j):
                            g[en].append(gen(i,j+1,c))
                        if cLeft(m,i,j):
                            g[en].append(gen(i,j-1,c))
                else:
                    if cDown(m,i,j):
                        g[en].append(gen(i+1,j,c))
                    if cUp(m,i,j):
                        g[en].append(gen(i-1,j,c))
                    if j==0:
                        if cRight(m,i,j):
                            g[en].append(gen(i,j+1,c))
                    elif j==c-1:
                        if cLeft(m,i,j):
                            g[en].append(gen(i,j-1,c))
                    else:
                        if cRight(m,i,j):
                            g[en].append(gen(i,j+1,c))
                        if cLeft(m,i,j):
                            g[en].append(gen(i,j-1,c))
    for i in g:
        g[i].sort()
    return g

def laDFS(g,start,path=[]):
    path=path+[start]
    for cell in g[start]:
        if cell not in path:
            path=laDFS(g,cell,path)
    return path

def minObstacles(maze):
    nRows=len(maze)
    nCols=len(maze[0])

    p1=[]
    p2=[]
    for i in range(0,nRows):
        for j in range(0,nCols):
            if maze[i][j]=="P":
                if p1:
                    p2.append(i)
                    p2.append(j)
                    break
                else:
                    p1.append(i)
                    p1.append(j)
        if p2:
            break

    #If next to each other
    if p1[0]==p2[0] and p2[1]-p1[1]==1:
        return -1
    if p1[1]==p2[1] and p2[0]-p1[0]==1:
        return -1

    #If dungeon is one row
    if nRows==1:
        for cell in range(p1[1]+1,p2[1]):
            if maze[0][cell]=="#":
                return 0
        return 1
    #If dungeon is one column
    if nCols==1:
        tm=[]
        for cell in range(p1[0]+1,p2[0]):
            tm.append(maze[cell][0])
        for cell in tm:
            if cell=="#":
                return 0
        return 1

    p1=gen(p1[0],p1[1],nCols)
    p2=gen(p2[0],p2[1],nCols)

    g=getAdjecencyList(maze,nRows,nCols)
 
    #Check if they are already separated
    if not g[p1]:
        return 0
    if not g[p2]:
        return 0
    if p2 not in laDFS(g,p1):
        return 0
    
    #One obstacle needed
    for o1 in g:
        if o1!=p1 and o1!=p2:
            temp=g[o1]
            g[o1]=[]
            if p2 not in laDFS(g,p1):
                return 1
            g[o1]=temp

    #Two obstacles needed
    for o1 in g:
        if o1!=p1 and o1!=p2:
            temp1=g[o1]
            g[o1]=[]
            for o2 in g:
                if o2!=p1 and o2!=p2 and o2!=p1:
                    temp2=g[o2]
                    g[o2]=[]
                    if p2 not in laDFS(g,p1):
                        return 2
                    g[o2]=temp2
            g[o1]=temp1

    #Three obstacles needed
    for o1 in g:
        if o1!=p1 and o1!=p2:
            temp1=g[o1]
            g[o1]=[]
            for o2 in g:
                if o2!=p1 and o2!=p2 and o2!=o1:
                    temp2=g[o2]
                    g[o2]=[]
                    for o3 in g:
                        if o3!=p1 and o3!=p2 and o3!=o1 and o3!=o2:
                            temp3=g[o3]
                            g[o3]=[]
                            if p2 not in laDFS(g,p1):
                                return 3
                            g[o3]=temp3
                    g[o2]=temp2
            g[o1]=temp1

    return 4

if __name__=="__main__":
    print(minObstacles(["P....","...##","##...","....P"]))
    print(minObstacles([".....",".P.P.","....."]))
    print(minObstacles([".#P.",".P#."]))

    print(minObstacles(["P.P."]))
    print(minObstacles(["P.#P."]))

    print(minObstacles(["P",".","#","P","#","."]))
    print(minObstacles(["P",".","P","."]))

    print(minObstacles(["####","#PP#","####"]))

    print(minObstacles(["...#.",".P#P.",".#...","...#.","....."]))