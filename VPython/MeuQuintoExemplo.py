from vpython import *
#Web VPython 3.2

def calculaY(posx,r):
    return sqrt(pow(r,2)
    -pow(posx-10,2))+10
    
planeta=sphere(pos=vector(10,10,0),
radius=5,color=vector(0,0,255))
lua=sphere(pos=vector(10,0,0),
radius=1,color=vector(128,128,128),make_trail=True, trail_radius=0.2,)
auxiliar = 1
i=0
while True:
    rate(60)
    
    if auxiliar<0:
        coordy = 20-calculaY(i,10)
        print("coordy:",coordy)
    else:
        coordy=calculaY(i,10)
        #print("coordy:",coordy)
    coordx=i
    lua.pos.x=coordx
    lua.pos.y=coordy
    
    planeta.pos.z = planeta.pos.z + 1
    lua.pos.z = lua.posz
    i = i+auxiliar
    if i==20:
        auxiliar = -1
    if i==0:
        auxiliar = 1

    