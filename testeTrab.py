from mn import *
import math

def f1(x): return math.exp(x) - 2
def df1(x): return math.exp(x)

print("\033[0;34mQA -=-=-=-=-=-=-=-=-=-=-=-\033[0m")
resp = newton(1.0, 0.0, f1, df1, 1e-12, 10)
historico_de_convergencia(resp)
# resp = newton_historico_x(1.0, 0.0, f1, df1, 1e-12, 10)

def f2(x): return x**3 - 2*x + 2
def df2(x): return 3*x**2 - 2

print("\033[0;34mQB -=-=-=-=-=-=-=-=-=-=-=-\033[0m")
resp = []
# resp = newton_historico_x(-1.5, 0.0, f2, df2, 1e-8, 20)
resp = newton(-1.5, 0.0, f2, df2, 1e-8, 20)
historico_de_convergencia(resp)

def f3(x): return x**3 - 3*x**2 + 4
def df3(x): return 3*x**2 - 6*x

print("\033[0;34mQC -=-=-=-=-=-=-=-=-=-=-=-\033[0m")
resp = []
# resp = newton_historico_x(2.0, 0.0, f3, df3, 1e-8, 10)
resp = newton(2.0, 0.0, f3, df3, 1e-8, 10)
historico_de_convergencia(resp)

def f4(x): return math.atan(x)
def df4(x): return 1/(1+x**2)

print("\033[0;34mQD -=-=-=-=-=-=-=-=-=-=-=-\033[0m")
resp = []
# resp = newton_historico_x(1.0, 0.0, f4, df4, 1e-12, 20)
resp = newton(1.0, 0.0, f4, df4, 1e-12, 20)
historico_de_convergencia(resp)

def f5(x): return (x-1)**2
def df5(x): return 2*(x-1)

print("\033[0;34mQE -=-=-=-=-=-=-=-=-=-=-=-\033[0m")
resp = []
# resp = newton_historico_x(3.0, 0.0, f5, df5, 1e-8, 30)
resp = newton(3.0, 0.0, f5, df5, 1e-8, 30)
historico_de_convergencia(resp)

def f6(x): return x**2 + 1
def df6(x): return 2*x
print("\033[0;34mQF -=-=-=-=-=-=-=-=-=-=-=-\033[0m")
resp = []
# resp = newton_historico_x(1.0, 0.0, f6, df6, 1e-8, 10)
resp = newton(1.0, 0.0, f6, df6, 1e-8, 10)
historico_de_convergencia(resp)