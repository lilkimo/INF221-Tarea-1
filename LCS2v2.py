# IMPORTANTE: Este script sólo corre en python >= 3.8
from typing import List, Match


def LCS(s,t):
    m = len(s)
    n = len (t)
    MemLCS = [ [ 0 for i in range(n+1) ] for j in range(m+1) ]
    MatchS = []
    MatchT = []
    for i in range( m+1 ):
        for j in range ( n+1 ):
            if j == 0 or i == 0:
                continue
            elif s[i-1] == t[j-1]:
                if MemLCS[i-1][j] != MemLCS[i][j-1]:
                    MemLCS[i][j] = max(MemLCS[i-1][j], MemLCS[i][j-1])
                else:
                    MemLCS[i][j] = MemLCS[i][j-1] + 1
                    MatchS.append(i-1)
                    MatchT.append(j-1)
            else:
                MemLCS[i][j] = max(MemLCS[i-1][j], MemLCS[i][j-1])
    
    return tuple([MatchS, MatchT])


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

def limpiar(matchS, matchT):
    j = -1
    i=0
    l = len(matchS)
    while i < l:
        if j < matchS[i]:
            j = matchS[i]
            i += 1
        else:
            matchT.pop(i)
            matchS.pop(i)
            l -= 1
    return tuple([matchS,matchT])


def main():
    s = 'BABA'
    t = 'A'
    print(min(
        differences(*limpiar(*LCS(s, t)), s, t),
        differences(*limpiar(*iLCS(s, t)), s, t),
        key = lambda x: len(x)
    ))
    
    
if __name__ == '__main__':
    main()
