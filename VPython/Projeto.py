from vpython import *
#Web VPython 3.2
from vpython import *
import random

# Função para detectar colisão entre dois objetos
def detecta_colisao(obj1, obj2):
    return abs(obj1.pos.x - obj2.pos.x) < (obj1.size.x/2 + obj2.size.x/2) and \
           abs(obj1.pos.y - obj2.pos.y) < (obj1.size.y/2 + obj2.size.y/2) and \
           abs(obj1.pos.z - obj2.pos.z) < (obj1.size.z/2 + obj2.size.z/2)

# Função para mover os objetos estáticos para posições aleatórias
def reposicionar_objeto(obj):
    obj.pos = vector(random.uniform(-largura/2, largura/2),
                     random.uniform(-altura/2, altura/2),
                     random.uniform(-profundidade/2, profundidade/2))

# Dimensões da área (2x maior)
largura = 100
altura = 60
profundidade = 60

# Desenhando a área como linhas finas
linha1 = curve(pos=[vector(-largura/2, -altura/2, -profundidade/2), vector(largura/2, -altura/2, -profundidade/2), vector(largura/2, altura/2, -profundidade/2), vector(-largura/2, altura/2, -profundidade/2), vector(-largura/2, -altura/2, -profundidade/2)], color=color.white)
linha2 = curve(pos=[vector(-largura/2, -altura/2, profundidade/2), vector(largura/2, -altura/2, profundidade/2), vector(largura/2, altura/2, profundidade/2), vector(-largura/2, altura/2, profundidade/2), vector(-largura/2, -altura/2, profundidade/2)], color=color.white)
linha3 = curve(pos=[vector(-largura/2, -altura/2, -profundidade/2), vector(-largura/2, -altura/2, profundidade/2)], color=color.white)
linha4 = curve(pos=[vector(largura/2, -altura/2, -profundidade/2), vector(largura/2, -altura/2, profundidade/2)], color=color.white)
linha5 = curve(pos=[vector(-largura/2, altura/2, -profundidade/2), vector(-largura/2, altura/2, profundidade/2)], color=color.white)
linha6 = curve(pos=[vector(largura/2, altura/2, -profundidade/2), vector(largura/2, altura/2, profundidade/2)], color=color.white)

# Criando polígonos
poligonos = [
    pyramid(pos=vector(-20, 0, 0), size=vector(4, 4, 4), color=color.red, make_trail=True, retain=50),  # Tetraedro
    box(pos=vector(20, 0, 0), size=vector(4, 4, 4), color=color.blue, make_trail=True, retain=50),  # Cubo
    pyramid(pos=vector(0, 10, 0), size=vector(4, 4, 4), color=color.green, make_trail=True, retain=50),  # Outro Tetraedro
    box(pos=vector(0, -10, 0), size=vector(4, 4, 4), color=color.yellow, make_trail=True, retain=50),  # Outro Cubo
    pyramid(pos=vector(0, 0, 10), size=vector(4, 4, 4), color=color.cyan, make_trail=True, retain=50),  # Outro Tetraedro
    box(pos=vector(0, 0, -10), size=vector(4, 4, 4), color=color.magenta, make_trail=True, retain=50),  # Outro Cubo
    pyramid(pos=vector(0, 0, 0), size=vector(4, 4, 4), color=color.orange, make_trail=True, retain=50)  # Outro Tetraedro
]

# Velocidades iniciais dos polígonos
velocidades = [
    vector(0.2, 0.1, 0.1),
    vector(-0.1, 0.2, -0.1),
    vector(0.1, -0.2, 0.1),
    vector(0.1, 0.1, -0.2),
    vector(-0.2, 0.1, 0.1),
    vector(0.1, -0.1, -0.2),
    vector(-0.1, -0.2, 0.2)
]

# Criando 10 objetos estáticos que aumentam a velocidade
objetos_estaticos = [
    sphere(pos=vector(random.uniform(-largura/2, largura/2), random.uniform(-altura/2, altura/2), random.uniform(-profundidade/2, profundidade/2)), radius=2, color=color.white) for _ in range(10)
]

# Temporizadores para controle do efeito de aumento de velocidade
tempo_aumento = [0] * len(poligonos)
duracao_aumento = 2  # Duração do aumento em segundos

while True:
    rate(60)
    
    for i in range(len(poligonos)):
        # Verificando se o efeito de aumento de velocidade deve terminar
        if tempo_aumento[i] > 0:
            tempo_aumento[i] -= 1/60  # Subtrai o tempo a cada frame (60 FPS)
            if tempo_aumento[i] <= 0:
                velocidades[i] /= fator_aumento
        
        # Movimento do polígono
        poligonos[i].pos += velocidades[i]
        
        # Checando colisão com os outros polígonos
        for j in range(i + 1, len(poligonos)):
            if detecta_colisao(poligonos[i], poligonos[j]):
                velocidades[i] = -velocidades[i]
                velocidades[j] = -velocidades[j]
        
        # Rebote nas bordas da área retangular
        if abs(poligonos[i].pos.x) > largura/2 - poligonos[i].size.x/2:
            velocidades[i].x = -velocidades[i].x
        if abs(poligonos[i].pos.y) > altura/2 - poligonos[i].size.y/2:
            velocidades[i].y = -velocidades[i].y
        if abs(poligonos[i].pos.z) > profundidade/2 - poligonos[i].size.z/2:
            velocidades[i].z = -velocidades[i].z
        
        # Checando colisão com os objetos estáticos
        for obj in objetos_estaticos:
            if detecta_colisao(poligonos[i], obj):
                if tempo_aumento[i] <= 0:
                    # Aumentar a velocidade temporariamente
                    fator_aumento = random.uniform(1.5, 2.5)
                    velocidades[i] *= fator_aumento
                    tempo_aumento[i] = duracao_aumento
                    
                    # Reposicionar o objeto estático aleatoriamente
                    reposicionar_objeto(obj)
