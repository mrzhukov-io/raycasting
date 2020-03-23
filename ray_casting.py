from ray_calculate import x_ray_calculation, y_ray_calculation
from render import render
x_player=9
y_player=5
FOV=120
POV=-20
world_map=[
"11111111111111111111",
"10000000100000001001",
"10000000100000000001",
"10000000100000000001",
"10000000000000000001",
"10000000000000000001",
"10000000000000000001",
"10000000000000000001",
"10000000000000000001",
"10000000000000000001",
"11111111111111111111"]
def raycasting(world_map, FOV, POV, x_player, y_player):
    distance=[]
    angle_offset=-FOV/2
    while angle_offset<FOV/2:
        ray_angle=angle_offset+POV
        S=1
        while S<10:           
            S+=1
            try:
                if (world_map[(int(x_ray_calculation(ray_angle, S)+x_player)-1)][(int(y_ray_calculation(ray_angle, S)+y_player)-1)]=="1"):
                    break
            except:
                S-=1
                break
        distance.append(S)
        angle_offset+=1
    return distance
if __name__=="__main__":
    while True:
        render(raycasting(world_map, FOV, POV, x_player, y_player))
        input("ENT")
     
