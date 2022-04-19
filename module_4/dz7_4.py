from turtle import distance


points = {
    (0, 1): 2,
    (0, 2): 3.8,
    (0, 3): 2.7,
    (1, 2): 2.5,
    (1, 3): 4.1,
    (2, 3): 3.9,
}

list=[0,1,3,2,0]

def calculate_distance(coordinates):
    distance=0
    if len(coordinates)==0:
        return 0
        
    for i in range(len(coordinates)-1):

        x=coordinates[i] 
        y=coordinates[i+1]
        if x>y:
            x,y=y,x
        distance+=points[(x,y)]

    return distance 
 


print(calculate_distance(list))