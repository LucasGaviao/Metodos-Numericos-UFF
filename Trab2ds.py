import numpy as np

def sistema_F(c, r, p):
    c1, c2, c3 = c
    return np.array([
        c1 * np.exp(c2 * r[0]) + c3 * r[0] - p[0],
        c1 * np.exp(c2 * r[1]) + c3 * r[1] - p[1],
        c1 * np.exp(c2 * r[2]) + c3 * r[2] - p[2]
    ])

def jacobiana(c, r):
    c1, c2, c3 = c
    J = np.zeros((3, 3))
    
    # Derivadas parciais para F1
    J[0, 0] = np.exp(c2 * r[0])          # df1/dc1
    J[0, 1] = c1 * r[0] * np.exp(c2 * r[0])  # df1/dc2
    J[0, 2] = r[0]                       # df1/dc3
    
    # Derivadas parciais para F2
    J[1, 0] = np.exp(c2 * r[1])
    J[1, 1] = c1 * r[1] * np.exp(c2 * r[1])
    J[1, 2] = r[1]
    
    # Derivadas parciais para F3
    J[2, 0] = np.exp(c2 * r[2])
    J[2, 1] = c1 * r[2] * np.exp(c2 * r[2])
    J[2, 2] = r[2]
    
    return J

def newton_raphson(c0, r, p, tol=1e-10, max_iter=6):
    c = c0.copy()
    historico = []
    historico.append(c)
    for k in range(max_iter):
        F = sistema_F(c, r, p)
        F = np.round(F, 4)
        if np.linalg.norm(F) < tol:
            print(f'Convergência alcançada na iteração {k}')
            break
        
        J = jacobiana(c, r)
        J = np.round(J, 4)
        try:
            delta = np.linalg.solve(J, F)
            delta = np.round(delta, 4)
        except np.linalg.LinAlgError:
            print("Jacobiana singular! Método falhou.")
            return None
        
        c -= delta
        c = np.round(c, 4)
        historico.append(c)
        print(f'\033[0;33mIteração {k}:\033[0m\nc{k+1} = {c}')
        print(f'F{k}: \033[0;35m{F}\033[0m')
        print(f'J{k}:\033[0;34m {J}\033[0m')
        print(f'Y{k}:\033[0;32m {delta}\033[0m')
        print(f'norma 1: \033[0;36m{np.linalg.norm(F, ord=1)}\033[0m')
        print(f'norma 2: \033[0;36m{np.linalg.norm(F)}\033[0m')
        print(f'norma inf: \033[0;36m{np.linalg.norm(F, ord=np.inf)}\033[0m')
    
    
    return c, historico

# Dados do problema
r = np.array([1.0, 2.0, 3.0])
p = np.array([10.0, 12.0, 15.0])
c0 = np.array([10.0, 1.0, -1.0])  # Chute inicial

# Executar o método
solucao, historico = newton_raphson(c0, r, p)

if solucao is not None:
    print('\nSolução final:')
    print(f'{solucao}')
    print(f'c1 = {solucao[0]:.4f}')
    print(f'c2 = {solucao[1]:.4f}')
    print(f'c3 = {solucao[2]:.4f}')
    print(f'F = {np.round(sistema_F(solucao, r, p), 4)}')
    print("=-=-=-=-=-=-=-=--=-=-=-=-=-=-")
    # for s in historico:
    #     print(f'c = {s}')
    #     f = np.round(sistema_F(s, r, p), 4)
    #     print(f'solução do sistema F:\033[0;35m{f}\033[0m')
    #     print(f'norma 2: \033[0;36m{np.linalg.norm(f)}\033[0m')
    #     print(f'norma inf: \033[0;36m{np.linalg.norm(f, ord=np.inf)}\033[0m')