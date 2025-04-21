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
        x1 = x0 - (f1(x0) / d1(x0))
        retorno[iteracao] = {
            "x0": x0,
            "x1": x1,
            "f(x0)": f1(x0),
            "f'(x0)": d1(x0),
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
