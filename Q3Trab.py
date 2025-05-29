from mn import *
from plt import *

def p1(x): return (x-1)*(x-2)*(x-3)*(x+1)
def dp1(x): return 4*x**3 - 15*x**2 + 10*x + 5

def p2(x): return (x-1)**2 * (x-2) * (x+1)
def dp2(x): return 4*x**3 - 9*x**2 + 2*x + 3

def p3(x): return (x-1)**3 * (x+2)
def dp3(x): return 4*x**3 - 3*x**2 - 6*x + 5

def raiz_unica(x0):
    p1 = lambda x: (x-1)*(x-2)*(x-3)*(x+1)
    dp1 = lambda x: 4*x**3 - 15*x**2 + 10*x + 5
    historico_p1 = newton_historico_x(x0, 0.0, p1, dp1, 1e-10, 100)
    print(historico_p1)
    plot_historico_vet(historico_p1)
    

def raiz_dupla(x0):
    p2 = lambda x: (x-1)**2 * (x-2) * (x+1)
    dp2 = lambda x: 4*x**3 - 9*x**2 + 2*x + 3
    historico_p2 = newton_historico_x(x0, 0.0, p2, dp2, 1e-10, 100)
    print(historico_p2)
    plot_historico_vet(historico_p2)


def raiz_tripla(x0):
    p3 = lambda x: (x-1)**3 * (x+2)
    dp3 = lambda x: 4*x**3 - 3*x**2 - 6*x + 5
    historico_p3 = newton_historico_x(x0, 0.0, p3, dp3, 1e-10, 100)
    print(historico_p3)
    plot_historico_vet(historico_p3)

x0 = 0.5
raiz_unica(x0)
raiz_dupla(x0)
raiz_tripla(x0)