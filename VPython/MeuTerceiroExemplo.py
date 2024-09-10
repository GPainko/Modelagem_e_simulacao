from vpython import *
#Web VPython 3.2

# Criação dos objetos
chao = box(pos=vec(0, 0, 0), length=200, height=1, width=1, color=color.green)
esfera = sphere(pos=vector(-100, 0, 0), radius=2, color=color.orange)

# Definindo o centro e o raio do movimento circular
centro = vector(0, 0, 0)
raio = 100  # Raio ajustado para percorrer toda a extensão da box

# Loop principal para movimentar a esfera em um arco da esquerda para a direita
for theta in range(0, 181):  # Movimenta de 0 a 180 graus (meia esfera)
    rate(120)  # Alta taxa de quadros para suavidade
    
    # Calcula a nova posição da esfera
    x = centro.x - raio * cos(radians(theta))
    y = centro.y + raio * sin(radians(theta)) 
    
    esfera.pos = vector(x, y, 0)
    
    # Desenhar a trajetória
    sphere(pos=esfera.pos, radius=0.2, color=color.white, opacity=0.6)