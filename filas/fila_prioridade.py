from random import randint
import time
# Starvation
# Lista para armazenar clientes com número e idade
clientes = []

# Gerar clientes com número e idade aleatórios
for i in range(10):
    numero = randint(1, 100)       # Número aleatório do cliente
    idade = randint(18, 90)        # Idade aleatória entre 18 e 90 anos
    clientes.append((numero, idade))

# Ordenar clientes com prioridade para os com idade acima de 69
clientes_prioridade = sorted(clientes, key=lambda x: x[1] < 70)

# Atender os clientes conforme a prioridade
for numero, idade in clientes_prioridade:
    inicio = time.perf_counter()  # Início da medição de tempo
    fim = time.perf_counter()     # Fim da medição de tempo
    tempo_leitura = fim - inicio  # Calcule o tempo que levou para ler o número
    prioridade = "com prioridade" if idade > 69 else "sem prioridade"
    print(f"Cliente {numero} (Idade: {idade}, {prioridade}) - Tempo de atendimento: {tempo_leitura:.8f} segundos")
