import numpy as np

def f1(x:float) -> float:
    return x**3 + 2

def bissecao(xl:float, xu:float, tol:float) -> list:
    fxu = f1(xu)
    fxl = f1(xl)
    iteracao = 1
    print(f"xl: {xl:.15f}, xu: {xu:.15f}, f(xl): {fxl:.15f}, f(xu): {fxu:.15f}")

    if fxu == 0.0:
        return xu
    elif fxl == 0.0:
        return xl
    elif fxu * fxl > 0.0:
        raise ValueError("Intervalo inválido")
    
    while not (abs(xu - xl) <= tol):
        print(f"Iteração: {iteracao}")
        xm = (xl + xu) / 2.0
        fxm = f1(xm)
        if fxm == 0.0:
            return xm
        elif fxm * fxl < 0.0:
            xu = xm
            fxu = fxm
        else:
            xl = xm
            fxl = fxm
        if iteracao == 2:
            residuo = abs(0 - fxm)
        print(f"xl: {xl:.15f}, xu: {xu:.15f}, f(xl): {fxl:.15f}, f(xu): {fxu:.15f}")
        iteracao += 1
        
    return [(xl + xu) / 2.0, iteracao-1, residuo]

xl = -2.0
xu = 1.0
tol = 0.2

print("QA -=-=-=-=-=-=-=-=-=-=-=-")
if f1(xl) * f1(xu) > 0.0:
    print("Intervalo inválido")
else:
    print("Intervalo válido")

resp = bissecao(xl, xu, tol)
print("QB -=-=-=-=-=-=-=-=-=-=-=-")
print(f'Sao necessarias {resp[1]} iterações')

print("QC -=-=-=-=-=-=-=-=-=-=-=-")
print(f"Residuo: {resp[2]:.15f}")