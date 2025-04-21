import numpy as np
from mn import *

def f1(x:float) -> float:
    return 1/x - 0.3

def bissecao(xl:float, xu:float, tol:float) -> list:
    fxu = f1(xu)
    fxl = f1(xl)
    iteracao = 0
    retorno = {}
    print(f"xl: {xl:.15f}, xu: {xu:.15f}, f(xl): {fxl:.15f}, f(xu): {fxu:.15f}")

    if fxu == 0.0:
        return xu
    elif fxl == 0.0:
        return xl
    elif fxu * fxl > 0.0:
        raise ValueError("Intervalo inválido")
    
    while iteracao < 4:
        print(f"Iteração: {iteracao}")
        xm = (xl + xu) / 2.0
        fxm = f1(xm)
        
        retorno[iteracao] = {
            "xl": xl,
            "xu": xu,
            "xm": xm,
            "er": erroRelativo(1/0.3, xm),
            "dr": desvioRelativo(xm, retorno[iteracao-1]["xm"]) if iteracao > 0 else float('inf'),
            "ra": residuoAbsoluto(f1(1/0.3), fxm)
        }
        
        if fxm == 0.0:
            return xm
        elif fxm * fxl < 0.0:
            xu = xm
            fxu = fxm
        else:
            xl = xm
            fxl = fxm
        print(f"xl: {xl:.15f}, xu: {xu:.15f}, f(xl): {fxl:.15f}, f(xu): {fxu:.15f}")
        iteracao += 1
        
    return retorno

xl = 2.0
xu = 6.0
tol = 0.2

resp = bissecao(xl, xu, tol)
print("QA -=-=-=-=-=-=-=-=-=-=-=-")
for i in resp.keys():
    print(f"Iteração {i}:")
    print(f"  xl: {resp[i]['xl']:.15f}")
    print(f"  xu: {resp[i]['xu']:.15f}")
    print(f"  xm: {resp[i]['xm']:.15f}")
    print(f"  Erro Relativo: {resp[i]['er']:.15f}")
    print(f"  Desvio Relativo: {resp[i]['dr']:.15f}")
    print(f"  Resíduo Absoluto: {resp[i]['ra']:.15f}")
    