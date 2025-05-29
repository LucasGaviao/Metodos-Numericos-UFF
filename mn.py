"""
A função newton será a função responsavel pela implementação do metodo de newton para uma função qualquer f1 e sua derivada d1.
"""
from typing import Callable, Dict

def erroAbsoluto(exato:float, aprox:float) -> float:
    return abs(exato - aprox)

def erroRelativo(exato:float, aprox:float) -> float:
    return abs((exato - aprox) / exato)

def residuoAbsoluto(fexato:float, faprox:float) -> float:
    return abs(fexato - faprox)

def residuoRelativo(fexato:float, faprox:float) -> float:
    return abs((fexato - faprox) / fexato)

def desvioAbsoluto(aprox1:float, aprox2:float) -> float:
    return abs(aprox1 - aprox2)

def desvioRelativo(aprox1:float, aprox2:float) -> float:
    if aprox1 != 0:
        return abs((aprox1 - aprox2) / aprox1)
    else:
        return aprox2

def newton_historico_x(x0:float, alpha:float, f1:Callable[[float], float], d1:Callable[[float], float], tol:float, maxit:int) -> list[float]:
    '''
    Explicando os parametros:
    x0: Chute inicial
    alpha: Valor que dejamos aproximar a função original f1
    f1: função original
    d1: derivada de f1
    tol: tolerancia de erro que servira como criterio para avaliar convergencia
    maxit: numero maximo de iterações

    Explicando saida:
    Será retornado uma lista como as aproximações de x apartir de x0.
    Exemplo: [x0, x1, x2 ... Xn], n <= maxit

    '''
    iteracao = 0 # contador de iterações 
    divergindo = False # flag de convegencia
    historico_x = [x0] # hitorico de x (retorno)
    historico_residuos = [residuoAbsoluto(0, (f1(x0)-alpha))] # historico de residuos sera usado para definir divergencia

    while iteracao < maxit:

        derivada_atual = d1(x0)
        # caso a derivada seja extremamaente pequena (muito proxima a 0)
        if abs(derivada_atual) < 1e-15:
          divergindo = True
          if divergindo:
            print(f"  \033[0;31mNão convergiu!\033[0m")
            return historico_x

        # formula de Newton-Raphson
        x1 = x0 - ((f1(x0)-alpha) / d1(x0))

        residuo_atual = residuoAbsoluto(0, (f1(x0)-alpha))
        historico_x.append(x1)
        historico_residuos.append(residuoAbsoluto(0, (f1(x0)-alpha)))

        '''
        Explicação da escolha dos critérios no proximo bloco.
        '''
        if len(historico_residuos) > 3:
            media_anterior = sum(historico_residuos[-4:-1])/3
            media_atual = sum(historico_residuos[-3:])/3
            if media_atual > media_anterior:
                divergindo = True

        # condição de satisfação
        if residuoAbsoluto(0, (f1(x0)-alpha)) < tol:
            break
        # atualizando o iterador e x0
        x0 = x1
        iteracao += 1
    if divergindo:
        print(f"  \033[0;31mO método divergiu!\033[0m")
    else:
      print("  \033[0;32mO método convergiu!\033[0m")
    return historico_x


''' Função pedida em Questão 2'''
def newton(x0:float, alpha:float, f1:Callable[[float], float], d1:Callable[[float], float], tol:float, maxit:int) -> Dict[str, Dict[str, float]]:
    iteracao = 0
    retorno = {}
    divergindo = False
    historico_x = [x0]
    historico_residuos = [residuoAbsoluto(0, (f1(x0)-alpha))]
    media_atual = float('nan')
    media_anterior = float('nan')

    while iteracao < maxit:
        
        residuo_atual = residuoAbsoluto(0, (f1(x0)-alpha))

        derivada_atual = d1(x0)
        # caso a derivada seja extremamaente pequena
        if abs(derivada_atual) < 1e-15:
            retorno[iteracao] = {
                "x0": x0,
                "x1": float('nan'),
                "f(x0)": (f1(x0)-alpha),
                "divergindo": False,
                "residuo":residuo_atual,
                "tolerancia":tol,
                "media_atual": media_atual,
                "media_anterior": media_anterior,
                "erro": "Derivada zero encontrada",
            }
            print(f"  \033[0;31mNão convergiu!\033[0m")
            return retorno

        # formula de Newton-Raphson
        x1 = x0 - ((f1(x0)-alpha) / d1(x0))

        historico_x.append(x1)
        historico_residuos.append(residuoAbsoluto(0, (f1(x0)-alpha)))

        if len(historico_residuos) > 3:
            media_anterior = sum(historico_residuos[-4:-1])/3
            media_atual = sum(historico_residuos[-3:])/3
            if media_atual > media_anterior:
                divergindo = True


        # informações que poderão ser acessadas no historico
        retorno[iteracao] = {
            "x0": x0,
            "x1": x1,
            "f(x0)": (f1(x0)-alpha),
            "divergindo": divergindo,
            "residuo":residuo_atual,
            "tolerancia":tol,
            "media_atual": media_atual,
            "media_anterior": media_anterior,
        }
        # condição de satisfação
        if residuoAbsoluto(0, (f1(x0)-alpha)) < tol:
            break
        # atualizando o iterador e x0
        x0 = x1
        iteracao += 1
    if divergindo:
        print(f"  \033[0;31mO método divergiu!\033[0m")
    else:
      print("  \033[0;32mO método convergiu!\033[0m")
    return retorno


def historico_de_convergencia(historico:Dict[str, Dict[str, float]]):
    for iteracao in historico:
        if  not historico[iteracao]['divergindo']:
            print(f'\033[0;34m{iteracao}°=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\033[0m')
        else:
            print(f'\033[0;31m{iteracao}°=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\033[0m')
        print(f"  x0: {historico[iteracao]['x0']:.15f}")
        print(f"  x1: {historico[iteracao]['x1']:.15f}")
        print(f"  f(x0): {historico[iteracao]['f(x0)']:.15f}")
        print(f"  divergindo: {historico[iteracao]['divergindo']}")
        print(f"  residuo: {historico[iteracao]['residuo']:.15f}")
        print(f"  tolerancia: {historico[iteracao]['tolerancia']}")
        print(f"  media_atual: {historico[iteracao]['media_atual']}")
        print(f"  media_anterior: {historico[iteracao]['media_anterior']}")
        if historico[iteracao]['x1'] == float('nan'):
            print(f"  erro: {historico[iteracao]['erro']}")
