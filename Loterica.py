import random
import time

for n1 in range(1, 55 + 1):
    for n2 in range(1 + n1, 56 + 1):
        for n3 in range(1 + n2, 57 + 1):
            for n4 in range(1 + n3, 58 + 1):
                for n5 in range(1 + n4, 59 + 1):
                    for n6 in range(1 + n5, 60 + 1):
                        time.sleep(0.1)
                        resultado = [n1, n2, n3, n4, n5, n6]
                        
                        random.shuffle(resultado)
                        print(' '.join(map(str, resultado)))
                        
                        
                        
                        #random.shuffle(resultado)
                        #