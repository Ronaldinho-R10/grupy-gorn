import threading
import time
import random

def simulate_game(match_id):
    # Simula a execução de uma partida de jogo
    duration = random.randint(1, 5)
    print(f"Partida {match_id}: Iniciada (Duração: {duration} segundos)")
    time.sleep(duration)
    print(f"Partida {match_id}: Encerrada")

if __name__ == '__main__':
    num_matches = 5  # Número de partidas a serem simuladas
    threads = []

    # Crie uma thread para cada partida
    for match_id in range(1, num_matches + 1):
        thread = threading.Thread(target=simulate_game, args=(match_id,))
        threads.append(thread)
        thread.start()

    # Aguarde todas as threads terminarem
    for thread in threads:
        thread.join()

    # Após todas as partidas terminarem
    print("Todas as partidas foram concluídas. Programa principal finalizado.")