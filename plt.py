import matplotlib.pyplot as plt
import numpy as np

def plot_historico_vet(historico):
    plt.plot(historico, 'o-')
    plt.xlabel('Iteração')
    plt.ylabel('Valor de x')
    plt.title('Convergência do Método de Newton')
    plt.grid()
    plt.show()

def plot_historico_dict(historico):
    historico_x = [v['x0'] for k, v in historico.items()]
    plt.plot(historico_x, 'o-')
    plt.xlabel('Iteração')
    plt.ylabel('Valor de x')
    plt.title('Convergência do Método de Newton')
    plt.grid()
    plt.show()

def plot_p1():
    x = np.linspace(-2, 4, 400)
    y = (x-1)*(x-2)*(x-3)*(x+1)

    plt.figure(figsize=(10,6))
    plt.plot(x, y, label='p₁(x) = (x-1)(x-2)(x-3)(x+1)')
    plt.axhline(0, color='black', linewidth=0.5)
    plt.scatter([-1,1,2,3], [0,0,0,0], color='red')
    plt.title('Polinômio com Raízes Simples (Cruzamento)')
    plt.legend()
    plt.grid()
    plt.show()

def plot_p2():
    x = np.linspace(-1.5, 3, 400)
    y = (x-1)**2 * (x-2) * (x+1)

    plt.figure(figsize=(10,6))
    plt.plot(x, y, label='p₂(x) = (x-1)²(x-2)(x+1)')
    plt.axhline(0, color='black', linewidth=0.5)
    plt.scatter([-1,1,2], [0,0,0], color='red')
    plt.title('Polinômio com Raiz Dupla em x=1 (Tangência)')
    plt.legend()
    plt.grid()
    plt.show()

def plot_p3():
    x = np.linspace(-2.5, 3, 400)
    y = (x-1)**3 * (x+2)

    plt.figure(figsize=(10,6))
    plt.plot(x, y, label='p₃(x) = (x-1)³(x+2)')
    plt.axhline(0, color='black', linewidth=0.5)
    plt.scatter([-2,1], [0,0], color='red')
    plt.title('Polinômio com Raiz Tripla em x=1 (Cruzamento com derivada zero)')
    plt.legend()
    plt.grid()
    plt.show()

