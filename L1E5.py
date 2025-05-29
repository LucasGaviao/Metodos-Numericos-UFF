from mn import *
from math import e


def f1(x:float) -> float:
    return x + 3*(e**(-x**2)) - 2

def derivada1(x:float) -> float:
    return 1 - 6*x*(e**(-x**2))


print("QA -=-=-=-=-=-=-=-=-=-=-=-")
x0 = -1.0
resp = newton(x0, 0.0, f1, derivada1, 1e-10, 5)
# for i in resp.keys():
#     print(f"Iteração {i}:")
#     print(f"  x0: {resp[i]['x0']:.15f}")
#     print(f"  x1: {resp[i]['x1']:.15f}")
#     print(f"  f(x0): {resp[i]['f(x0)']:.15f}")
#     print(f"  d(x0): {resp[i]['d(x0)']:.15f}")
#     print(f"  Desvio Absoluto: {resp[i]['desvioAbsoluto']:.15f}")
#     print(f"  Resíduo Absoluto: {resp[i]['residuoAbsoluto']:.15f}")
historico_de_convergencia(resp)

print("QB -=-=-=-=-=-=-=-=-=-=-=-")
x0 = 0.3
resp.clear()
resp = newton(x0, 0.0, f1, derivada1, 1e-10, 20)
historico_de_convergencia(resp)
