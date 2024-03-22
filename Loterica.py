import random
import time

probability_chances = []

for n1 in range(1, 55 + 1):
    for n2 in range(1 + n1, 56 + 1):
        for n3 in range(1 + n2, 57 + 1):
            for n4 in range(1 + n3, 58 + 1):
                for n5 in range(1 + n4, 59 + 1):
                    for n6 in range(1 + n5, 60 + 1):
                        time.sleep(0.1)
                        resultado = [n1, n2, n3, n4, n5, n6]
                        random.shuffle(resultado)
                        
                        if 10 in [n1, n2, n3, n4, n5, n6] or 24 in [n1, n2, n3, n4, n5, n6]:
                            notification = '================\nSequência armazenada!\n================'
                            probability_chances.append(resultado)
                            print(notification)
                            
                        print(' '.join(map(str, resultado)))
                        
                        
                    