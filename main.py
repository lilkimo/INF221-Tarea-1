# IMPORTANTE: Este script sólo corre en python >= 3.8
from typing import List

def LCS(s: str, t: str, dp: List = ...) -> List:
    n, m = len(s) - 1, len(t) - 1
    if dp == ...:
        dp = [[None for i in range(m + 1)] for i in range(n + 1)]
    if n == -1 or m == -1:
        return ([], [])
    if dp[n][m] != None:
        return dp[n][m]
    
    if s[-1] == t[-1]:
        temp = LCS(s[:-1], t[:-1], dp)
        dp[n][m] = (temp[0] + [n], temp[1] + [m])
    else:
        dp[n][m] = max(
            LCS(s, t[:-1], dp),
            LCS(s[:-1], t, dp),
            key = lambda x: len(x[0])
        )
    return dp[n][m]

# Un ligero truco para que LCS recorra de izquierda a derecha en vez de derecha a izquierda.
def iLCS(s: str, t: str) -> List:
    # Básicamente damos vuelta la palabra y LCS recorre la palabra invertida de derecha a izquierda,
    # luego damos vuelta los resultados y la palabra, logrando así que la palabra se recorriese de izquierda a derecha.
    iWay = list(LCS(s[::-1], t[::-1]))
    iWay[0] = list(map(lambda x: len(s)-x-1, iWay[0]))[::-1]
    iWay[1] = list(map(lambda x: len(t)-x-1, iWay[1]))[::-1]
    return tuple(iWay)

def differences(matchS: List[int], matchT: List[int], s: str, t: str) -> List:
    matchS, matchT = [-1] + matchS + [len(s)], [-1] + matchT + [len(t)]
    diffs = []
    i = 0
    while (i := i + 1) < len(matchS):
        if (diff := (s[matchS[i-1] + 1:matchS[i]], t[matchT[i-1] + 1:matchT[i]])) != ('', ''):
            diffs.append(diff)
    return diffs

# Permite al usuario hacer ingreso de sus propios casos de prueba
def misPruebas():
    while True:
        l1 = input("Ingrese primera palabra: ")
        l2 = input("Ingrese segunda palabra: ")
        if l1 == '-1' and l2 == '-1':
            break
        lst = min(
            differences(*LCS(l1, l2), l1, l2),
            differences(*iLCS(l1, l2), l1, l2),
            key = lambda x: len(x)
            )
        print(len(lst))
        for y in lst:
            print(" ".join(y))

# Permite al usuario leer un archivo con casos de prueba.
def lecturaInput(archivo):
    with open (archivo, 'r') as txt:
        repeticiones = int(txt.readline())
        for x in range(repeticiones):
            l1 = " ".join(txt.readline().strip().split()[1:])
            l2 = " ".join(txt.readline().strip().split()[1:])
            lst = min(
                differences(*LCS(l1, l2), l1, l2),
                differences(*iLCS(l1, l2), l1, l2),
                key = lambda x: len(x)
                )
            print(len(lst))
            for y in lst:
                print(" ".join(y))

def main():
    lecturaInput('input-1.txt')
    com = input("Desea ingresar sus propias pruebas? (y): ")
    if com == 'y':
        misPruebas()

if __name__ == '__main__':
    main()

#COMENTARIO
#ESTO ES UN COMENTARIO


