import concurrent.futures
import time
import random

def mail_letter(letter):
    duration = random.randint(1, 5)
    print(f"Started mailing letter {letter} (duration: {duration}s)")
    time.sleep(duration)
    print(f"Finished mailing letter {letter}")
    return f"Letter {letter} mailed"

if __name__ == '__main__':
    letters = ['A', 'B', 'C', 'D', 'E']

    # ThreadPoolExecutor is ideal for I/O-bound tasks
    # ThreadPoolExecutor is like having multiple chefs in a shared kitchen

    # Creates a ThreadPoolExecutor instance as a context manager, which manages the life cycle of a pool of worker threads that will be used to execute tasks concurrently.
    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = list(executor.map(mail_letter, letters))


    # Em vez de usar threads, concurrent.futures usa processos. Cada processo tem seu próprio interpretador Python e, portanto, não é afetado pelo GIL. Isso permite que você execute código em paralelo de forma mais eficaz em sistemas multi-core, sem as restrições impostas pelo GIL nas threads    
    print("Mailing Results:")
    for result in results:
        print(result)