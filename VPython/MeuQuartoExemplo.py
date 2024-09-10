from vpython import *
#Web VPython 3.2

# Criação dos objetos
caixa1 = box(pos=vec(0, 0, 0), length=10, height=1, width=1, color=color.white)
caixa2 = box(pos=vec(25, 25, 0), length=10, height=5, width=1, color=color.white)
caixa3 = box(pos=vec(-25, 25, 0), length=10, height=5, width=1, color=color.white)
esfera = sphere(pos=vector(50, 0, 0), radius=2, color=color.orange)

# Definindo o centro e o raio do movimento circular
centro = vector(0, 0, 0)
raio = 50

# Loop principal para movimentar a esfera em um arco esférico completo (0 a 360 graus)
for theta in range(0, 361):  # Movimenta de 0 a 360 graus (volta completa)
    rate(120)  # Alta taxa de quadros para suavidade
    
    # Calcula a nova posição da esfera
    x = centro.x - raio * cos(radians(theta))  # Movimentação em torno do eixo X
    y = centro.y + raio * sin(radians(theta))  # Movimentação em torno do eixo Y
    z = centro.z + raio * sin(radians(theta))  # Adiciona movimento no plano Z
    
    esfera.pos = vector(x, y, z)
    
    # Desenhar a trajetória
    sphere(pos=esfera.pos, radius=0.2, color=color.white, opacity=0.6)