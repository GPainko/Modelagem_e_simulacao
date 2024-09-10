from vpython import *
#Web VPython 3.2
esquerda = box(pos=vec(-10, 0, 0),length=1, height=1, width=1, color=color.blue)

direita = box(pos=vec(10, 0, 0),length=1, height=1, width=1, color=color.red)

esfera = sphere(pos=vector(0,0,0),radius=1,color=color.orange)

while True:
    while True:
        rate(60)
        if esfera.pos.x < direita.pos.x - 2:  
            esfera.pos.x += 1
        else:
            break  
    
    while True:
        rate(60)
        if esfera.pos.x > esquerda.pos.x + 2:  
            esfera.pos.x -= 1
        else:
            break  