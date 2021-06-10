# IMPORTANTE: Este script sólo corre en python >= 3.8
from typing import List

def LCS(s: str, t: str) -> List:
    if len(s) == 0 or len(t) == 0:
        return ([], [])
    if s[-1] == t[-1]:
        temp = LCS(s[:-1], t[:-1])
        return (temp[0] + [len(s) - 1], temp[1] + [len(t) - 1])
    return max(
        LCS(s, t[:-1]),
        LCS(s[:-1], t),
        key = lambda x: len(x[0])
    )

# Un ligero truco para que LCS recorra de izquierda a derecha en vez de derecha a izquierda.
def iLCS(s: str, t: str):
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

def main():
    s = 'Este es un texto'
    t = 'Este es otro texto'
    print(min(
        differences(*LCS(s, t), s, t),
        differences(*iLCS(s, t), s, t),
        key = lambda x: len(x)
    ))

if __name__ == '__main__':
    main()
