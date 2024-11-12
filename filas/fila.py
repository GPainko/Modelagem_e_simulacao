from random import randint
import time

clientes = []
for i in range(10):
    cliente = randint(1,100)
    clientes.append(cliente)

for numero in clientes:
    inicio = time.perf_counter()  # Início da medição de tempo
    fim = time.perf_counter()  # Fim da medição de tempo
    tempo_leitura = fim - inicio  # Calcule o tempo que levou para ler o número
    print(f"Tempo para atender o cliente {numero}: {tempo_leitura:.8f} segundos")