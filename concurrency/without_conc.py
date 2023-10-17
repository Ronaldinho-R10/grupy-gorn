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
    results = []

    for letter in letters:
        result = mail_letter(letter)
        results.append(result)

    print("Mailing Results:")
    for result in results:
        print(result)