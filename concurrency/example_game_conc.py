import concurrent.futures
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

    with concurrent.futures.ProcessPoolExecutor() as executor:
        # Crie processos para simular as partidas
        match_ids = list(range(1, num_matches + 1))
        executor.map(simulate_game, match_ids)

    # Após todas as partidas terminarem
    print("Todas as partidas foram concluídas. Programa principal finalizado.")