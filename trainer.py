import random

matrix=[[1,1,1,1],[1,0,0,1],[-1,0,0,-1],[-1,-1,-1,-1]]
position=[-1,-1]
savemove=[[position,position]]*10
savecount=0

def state(position):
    if position[0]<0 or position[0]>3 or position[1]<0 or position[1]>3:
        return -100
    else:
        return matrix[position[0]][position[1]]

def move_random(theturn):  #theturn 表示轮到谁下
    global savecount
    global position
    global savemove
    nextposition,moveposition=[-10,-10],[-10,-10]
    while state(position)!=theturn or state(nextposition)!=0:
        position=[random.randint(0,3),random.randint(0,3)]
        moveposition=random.choice([[-1,0],[1,0],[0,-1],[0,1]]) #分别对应上，下，左，右
        nextposition=[position[0]+moveposition[0],position[1]+moveposition[1]]

    matrix[position[0]][position[1]]=0
    matrix[nextposition[0]][nextposition[1]]=theturn
    savemove[savecount]=[position,nextposition]
    savecount+=1

    checkmove(savemove[savecount-1])

def checkmove(themove):
    #this is checkmove




def move_human():
    matrix[:]=[[1,1,1,1],[1,0,0,1],[-1,0,0,-1],[-1,-1,-1,-1]]
    savemove[1]=[[1,1,],[2,2]]

