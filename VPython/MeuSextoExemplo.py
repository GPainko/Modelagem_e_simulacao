from vpython import *
#Web VPython 3.2

esfera = sphere(pos = vector(0,0,0), radius = 1,color=color.red)
direito = box(pos = vector(10,0,0),width = 1,color=color.blue)
esquerdo = box(pos = vector(-10,0,0),width = 1,color=color.blue)

bee = esfera.pos.x - esfera.radius
bde = esfera.pos.x + esfera.radius

bordaDireita = esquerdo.pos.x + (esquerdo.width/2)
bordaEsquerda = direito.pos.x - (direito.width/2)

while True:
    rate(60)
    if bde < bordaEsquerda:
        esfera.pos.x += 1
    elif bde == bordaEsquerda:
        esfera.pos.x -= 1
    else:
        break
