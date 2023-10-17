import logging
import threading
import time


# Script para criação de uma única thread que executa em parelelo a outra thread

def thread_function(name):
    logging.info("Thread %s: starting", name)
    time.sleep(2)
    logging.info("Thread %s: finishing", name)

if __name__ == "__main__":

    # defini como as informações serão salvas no log
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    logging.info("Main    : before creating thread")

    # Aqui, uma nova instância de uma thread é criada. A função thread_function será executada nesta thread, e é passado um argumento (1) para essa função

    #x = threading.Thread(target=thread_function, args=(1,))

    # ma thread de daemon se encerrará imediatamente quando o programa for encerrado. Uma maneira de entender essas definições é considerar a thread de daemon como uma thread que é executada em segundo plano sem a preocupação de encerrá-la explicitamente
    x = threading.Thread(target=thread_function, args=(1,), daemon=True)

    logging.info("Main    : before running thread")

    # Inicia a thread e executada a função theread funciton em paralelo a execução principal

    x.start()
    
    logging.info("Main    : wait for the thread to finish")
    # x.join() permitiria que a execução principal aguardasse a conclusão da thread secundária antes de continuar

    # x.join()

    logging.info("Main    : all done")