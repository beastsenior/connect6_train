matrix=[[1,1,1,1],[1,0,0,1],[-1,0,0,-1],[-1,-1,-1,-1]]
nextmove=[[0,0],[0,0]]

def human():
    matrix[:]=[[0,1,1,1],[1,0,0,1],[-1,0,0,-1],[-1,-1,-1,-1]]
    nextmove[:]=[[1,1,],[2,2]]
    print(matrix)