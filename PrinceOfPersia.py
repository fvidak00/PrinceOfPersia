def imaLiPuta(a,b,tm,rows,cols):
    r=a
    c=b
    tm[r][c]="#"
    br=4
    while(br>0):
        if(br==4 and c<cols-1):
            if(c+1<cols and tm[r][c+1]!="#"):
                c+=1
                if(tm[r][c]=="P"):
                    return -1
                tm[r][c]="#"
            elif(r+1<rows and tm[r+1][c]!="#"):
                r+=1
                if(tm[r][c]=="P"):
                    return -1
                tm[r][c]="#"
            elif(c-1>-1 and tm[r][c-1]!="#"):
                c-=1
                if(tm[r][c]=="P"):
                    return -1
                tm[r][c]="#"
            elif(r-1>-1 and tm[r-1][c]!="#"):
                r-=1
                if(tm[r][c]=="P"):
                    return -1
                tm[r][c]="#"
            else:
                br-=1
                r=a
                c=b
        elif(br==3 and r<rows-1):
            if(c+1<cols and tm[r][c+1]!="#"):
                c+=1
                if(tm[r][c]=="P"):
                    return -1
                tm[r][c]="#"
            elif(r+1<rows and tm[r+1][c]!="#"):
                r+=1
                if(tm[r][c]=="P"):
                    return -1
                tm[r][c]="#"
            elif(c-1>-1 and tm[r][c-1]!="#"):
                c-=1
                if(tm[r][c]=="P"):
                    return -1
                tm[r][c]="#"
            elif(r-1>-1 and tm[r-1][c]!="#"):
                r-=1
                if(tm[r][c]=="P"):
                    return -1
                tm[r][c]="#"
            else:
                br-=1
                r=a
                c=b
        elif(br>2):
            br-=1
        elif(br<=2):
            if(c+1<cols and tm[r][c+1]!="#"):
                c+=1
                if(tm[r][c]=="P"):
                    return -1
                tm[r][c]="#"
            elif(r+1<rows and tm[r+1][c]!="#"):
                r+=1
                if(tm[r][c]=="P"):
                    return -1
                tm[r][c]="#"
            elif(c-1>-1 and tm[r][c-1]!="#"):
                c-=1
                if(tm[r][c]=="P"):
                    return -1
                tm[r][c]="#"
            elif(r-1>-1 and tm[r-1][c]!="#"):
                r-=1
                if(tm[r][c]=="P"):
                    return -1
                tm[r][c]="#"
            else:
                br-=1
                r=a
                c=b
        else:
            br-=1
    return br

def minObstacles(maze):
    rows=len(maze)
    cols=len(maze[0])
    br=0
    posP=[]

    # Find Prince and/or Princess
    while (br<2):
        for i in range(0,rows):
            for j in range(0,cols):
                if(maze[i][j]=="P"):
                    posP.append([i,j])
                    br+=1
                if (br==2):
                    break
            if(br==2):
                break
    # If they are in the same row next to each other
    if(posP[0][0]==posP[1][0] and (posP[1][1]-posP[0][1])==1):
        return -1
    # If they are in the same column next to each other
    if(posP[0][1]==posP[1][1] and (posP[1][0]-posP[0][0])==1):
        return -1
    # If cell is one row
    if(rows==1):
        obs=[o for o, h in enumerate(maze[0]) if h=="#"]
        for i in obs:
            if (i>posP[0][1] and i<posP[1][1]):
                return 0
        return 1
    # If cell is one column
    if(cols==1):
        obs=[]
        for i in range(0,rows):
            if(maze[i]=="#"):
                obs.append(i)
        for i in obs:
            if(i>posP[0][0] and i<posP[1][0]):
                return 0
        return 1
    # Else
    minObs=10
    #Gornji livi ćošak
    if(maze[0][0]=="P"):
        if(maze[0][1]!="#" and maze[1][0]!="#"):
            if(minObs>2):
                minObs=2
        elif(maze[0][1]=="#" and maze[1][0]=="#"):
            return 0
        elif(maze[0][1]=="#" or maze[1][0]=="#"):
            if(minObs>1):
                minObs=1
    #Gornji desni ćošak
    if(maze[0][cols-1]=="P"):
        if(maze[0][cols-2]=="#" and maze[1][cols-1]=="#"):
            return 0
        elif(maze[0][cols-2]!="#" and maze[1][cols-1]!="#"):
            if(minObs>2):
                minObs=2
        elif(maze[0][cols-2]=="#" or maze[1][cols-1]=="#"):
            if(minObs>1):
                minObs=1
    #Donji livi ćošak
    if(maze[rows-1][0]=="P"):
        if(maze[rows-1][1]=="#" and maze[rows-2][0]=="#"):
            return 0
        elif(maze[rows-1][1]!="#" and maze[rows-2][0]!="#"):
            if(minObs>2):
                minObs=2
        elif(maze[rows-1][1]=="#" or maze[rows-2][0]=="#"):
            if(minObs>1):
                minObs=1
    #Donji desni ćošak
    if(maze[rows-1][cols-1]=="P"):
        if(maze[rows-1][cols-2]=="#" and maze[rows-2][cols-1]=="#"):
            return 0
        elif(maze[rows-1][cols-2]!="#" and maze[rows-2][cols-1]!="#"):
            if(minObs>2):
                minObs=2
        elif(maze[rows-1][cols-2]=="#" or maze[rows-2][cols-1]=="#"):
            if(minObs>1):
                minObs=1
    #Gornji red, ali ne ćoškovi
    if(posP[0][0]==0 and posP[0][1]!=0 and posP[0][1]!=cols-1):
        br=3
        if(maze[0][posP[0][1]-1]=="#"):
            br-=1
        if(maze[0][posP[0][1]+1]=="#"):
            br-=1
        if(maze[1][posP[0][1]]=="#"):
            br-=1
        if(minObs>br):
            minObs=br
    if(posP[1][0]==0 and posP[1][1]!=0 and posP[1][1]!=cols-1):
        br=3
        if(maze[0][posP[1][1]-1]=="#"):
            br-=1
        if(maze[0][posP[1][1]+1]=="#"):
            br-=1
        if(maze[1][posP[1][1]]=="#"):
            br-=1
        if(br==0):
            return 0
        if(minObs>br):
            minObs=br
    #Donji red, ali ne ćoškovi
    if(posP[0][0]==rows-1 and posP[0][1]!=0 and posP[0][1]!=cols-1):
        br=3
        if(maze[rows-1][posP[0][1]-1]=="#"):
            br-=1
        if(maze[rows-1][posP[0][1]+1]=="#"):
            br-=1
        if(maze[rows-2][posP[0][1]]=="#"):
            br-=1
        if(br==0):
            return 0
        if(minObs>br):
            minObs=br
    if(posP[1][0]==rows-1 and posP[1][1]!=0 and posP[1][1]!=cols-1):
        br=3
        if(maze[rows-1][posP[1][1]-1]=="#"):
            br-=1
        if(maze[rows-1][posP[1][1]+1]=="#"):
            br-=1
        if(maze[rows-2][posP[1][1]]=="#"):
            br-=1
        if(br==0):
            return 0
        if(minObs>br):
            minObs=br
    #Livi stupac, ali ne ćoškovi
    if(posP[0][1]==0 and posP[0][0]!=0 and posP[0][0]!=rows-1):
        br=3
        if(maze[posP[0][0]-1][0]=="#"):
            br-=1
        if(maze[posP[0][0]+1][0]=="#"):
            br-=1
        if(maze[posP[0][0]][1]=="#"):
            br-=1
        if(br==0):
            return 0
        if(minObs>br):
            minObs=br
    if(posP[1][1]==0 and posP[1][0]!=0 and posP[1][0]!=rows-1):
        br=3
        if(maze[posP[1][0]-1][0]=="#"):
            br-=1
        if(maze[posP[1][0]+1][0]=="#"):
            br-=1
        if(maze[posP[1][0]][0]=="#"):
            br-=1
        if(br==0):
            return 0
        if(minObs>br):
            minObs=br
    #Desni stupac, ali ne ćoškovi
    if(posP[0][1]==cols-1 and posP[0][0]!=0 and posP[0][0]!=rows-1):
        br=3
        if(maze[posP[0][0]-1][cols-1]=="#"):
            br-=1
        if(maze[posP[0][0]+1][cols-1]=="#"):
            br-=1
        if(maze[posP[0][0]][cols-2]=="#"):
            br-=1
        if(br==0):
            return 0
        if(minObs>br):
            minObs=br
    if(posP[1][1]==cols-1 and posP[1][0]!=0 and posP[1][0]!=rows-1):
        br=3
        if(maze[posP[1][0]-1][cols-1]=="#"):
            br-=1
        if(maze[posP[1][0]+1][cols-1]=="#"):
            br-=1
        if(maze[posP[1][0]][cols-2]=="#"):
            br-=1
        if(br==0):
            return 0
        if(minObs>br):
            minObs=br
    #Okruženje
    if(posP[0][0]!=0 and posP[0][0]!=rows-1 and posP[0][1]!=0 and posP[0][1]!=cols-1):
        br=4
        if(maze[posP[0][0]][posP[0][1]-1]=="#"):
            br-=1
        if(maze[posP[0][0]][posP[0][1]+1]=="#"):
            br-=1
        if(maze[posP[0][0]-1][posP[0][1]]=="#"):
            br-=1
        if(maze[posP[0][0]+1][posP[0][1]]=="#"):
            br-=1
        if(br==0):
            return 0
        if(minObs>br):
            minObs=br
    if(posP[1][0]!=0 and posP[1][0]!=rows-1 and posP[1][1]!=0 and posP[1][1]!=cols-1):
        br=4
        if(maze[posP[1][0]][posP[1][1]-1]=="#"):
            br-=1
        if(maze[posP[1][0]][posP[1][1]+1]=="#"):
            br-=1
        if(maze[posP[1][0]-1][posP[1][1]]=="#"):
            br-=1
        if(maze[posP[1][0]+1][posP[1][1]]=="#"):
            br-=1
        if(br==0):
            return 0
        if(minObs>br):
            minObs=br
    #Ima li puta?
    tm=[]
    tm2=[]
    for i in range(0,rows):
        tm.append([])
        for j in range(0,cols):
            tm[i].append(maze[i][j])
    for i in range(0,rows):
        tm2.append([])
        for j in range(0,cols):
            tm2[i].append(maze[i][j])

    imala=imaLiPuta(posP[0][0],posP[0][1],tm,rows,cols)
    if(imala==0):
        print(tm2)
        imalb=imaLiPuta(posP[1][0],posP[1][1],tm2,rows,cols)
        if(imalb==0):
            return 0
    #Ako ima puta
    ListObs=[]
    for r in range(0,rows):
        obs=[o for o, h in enumerate(maze[r]) if h=="#"]
        ListObs.append(obs)
    #Ako nema prepreka
    br=0
    for i in ListObs:
        if not i:
            br+=1
        else:
            break
    if(br==rows):
        #Ako su u istom redu
        if(posP[0][0]==posP[1][0]):
            if (minObs>rows):
                minObs=rows
            return minObs
        #...stupcu
        if(posP[0][1]==posP[1][1]):
            if (minObs>cols):
                minObs=cols
            return minObs


    return -2

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