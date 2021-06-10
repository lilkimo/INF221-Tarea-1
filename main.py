# IMPORTANTE: Este script sólo corre en python >= 3.8
from typing import List

def LCS(s: str, t: str) -> int:
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

def differences(matchS: List[int], matchT: List[int], s: str, t: str) -> List:
    matchS, matchT = [-1] + matchS + [len(s)], [-1] + matchT + [len(t)]
    diffs = []
    i = 0
    while (i := i + 1) < len(matchS):
        if (diff := (s[matchS[i-1] + 1:matchS[i]], t[matchT[i-1] + 1:matchT[i]])) != ('', ''):
            diffs.append(diff)
    return diffs

def main():
    s = 'ABCLGH'
    t = 'AELFHR'
    print(LCS(s, t)[0])
    print(LCS(s, t)[1])
    #print(differences(*LCS(s, t), s, t))

if __name__ == '__main__':
    main()
