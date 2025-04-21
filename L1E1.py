import numpy as np

vet = np.array([2.0, 1.5, 1.4166666666666665, 1.4142156862745097, 1.4142135623746899])
desvio = np.array([])
for i in range(1, len(vet)):
    desvio = np.append(desvio, abs(vet[i] - vet[i-1]))

print("QA -=-=-=-=-=-=-=-=-=-=-=-")
for d in desvio:
    print(f'{d:.20f}')
    
print("QB -=-=-=-=-=-=-=-=-=-=-=-")
for i in range(0, len(vet)-1):
    desvio[i] = desvio[i] / vet[i]
    print(f'{desvio[i]:.20f}')
    
print("QC -=-=-=-=-=-=-=-=-=-=-=-")
exato = np.sqrt(2)
erro = np.array([])
for i in range(0, len(vet)-1):
    erro = np.append(erro, abs(exato - vet[i]))
    print(f'{erro[i]:.20f}')

print("QD -=-=-=-=-=-=-=-=-=-=-=-")
for i in range(0, len(vet)-1):
    erro[i] = erro[i] / exato
    print(f'{erro[i]:.20f}')
    