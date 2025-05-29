from typing import Callable, Dict

def erroAbsoluto(exato:float, aprox:float) -> float:
    return abs(exato - aprox)

def erroRelativo(exato:float, aprox:float) -> float:
    return abs((exato - aprox) / exato)

def residuoAbsoluto(exato:float, aprox:float) -> float:
    return abs(exato - aprox)

def residuoRelativo(exato:float, aprox:float) -> float:
    return abs((exato - aprox) / exato)

def desvioAbsoluto(aprox1:float, aprox2:float) -> float:
    return abs(aprox1 - aprox2)

def desvioRelativo(aprox1:float, aprox2:float) -> float:
    return abs((aprox1 - aprox2) / aprox1)

def newton(x0:float, f1:Callable[[float], float], d1:Callable[[float], float], tol:float, maxit:int) -> Dict[str, Dict[str, float]]:
    iteracao = 0
    retorno = {}
    # print(f"x0: {x0:.15f}, f(x0): {f1(x0):.15f}, f'(x0): {derivada1(x0):.15f}")

    while iteracao < maxit:
        # print(f"Iteração: {iteracao}")
        x1 = x0 - (f1(x0)/ d1(x0))
        retorno[iteracao] = {
            "x0": x0,
            "x1": x1,
            "f(x0)": f1(x0),
            "d(x0)": d1(x0),
            "desvioAbsoluto": desvioAbsoluto(x1, x0),
            "desvioRelativo": desvioRelativo(x1, x0),
            "residuoAbsoluto": residuoAbsoluto(0, f1(x1)),
        }
        
        if residuoAbsoluto(0, f1(x1)) < tol:
            break
        # print(f"x0: {x0:.15f}, x1: {x1:.15f}, f(x0): {f1(x0):.15f}, f'(x0): {derivada1(x0):.15f}")
        x0 = x1
        iteracao += 1
        
    return retorno

from math import e


def f1(x:float) -> float:
    return x + 3*(e**(-x**2)) - 2

def derivada1(x:float) -> float:
    return 1 - 6*x*(e**(-x**2))


print("QA -=-=-=-=-=-=-=-=-=-=-=-")
x0 = -1.0
resp = newton(x0, f1, derivada1, 1e-10, 5)
for i in resp.keys():
    print(f"Iteração {i}:")
    print(f"  x0: {resp[i]['x0']:.15f}")
    print(f"  x1: {resp[i]['x1']:.15f}")
    print(f"  f(x0): {resp[i]['f(x0)']:.15f}")
    print(f"  d(x0): {resp[i]['d(x0)']:.15f}")
    print(f"  Desvio Absoluto: {resp[i]['desvioAbsoluto']:.15f}")
    print(f"  Resíduo Absoluto: {resp[i]['residuoAbsoluto']:.15f}")

print("QB -=-=-=-=-=-=-=-=-=-=-=-")
x0 = 0.3
resp.clear()
resp = newton(x0, f1, derivada1, 1e-10, 5)
for i in resp.keys():
    print(f"Iteração {i}:")
    print(f"  x0: {resp[i]['x0']:.15f}")
    print(f"  x1: {resp[i]['x1']:.15f}")
    print(f"  f(x0): {resp[i]['f(x0)']:.15f}")
    print(f"  d(x0): {resp[i]['d(x0)']:.15f}")
    print(f"  Desvio Absoluto: {resp[i]['desvioAbsoluto']:.15f}")
    print(f"  Resíduo Absoluto: {resp[i]['residuoAbsoluto']:.15f}")