from numpy import array, zeros
from numpy.linalg import solve
d = [0,1,2,3,4,5,6,7,8,9]
m = zeros((4,4))
count = 0
r1 = range(10)
r2 = range(100)
firstpiece = []
for a in r1:
    for b in r1:
        for c in r1:
            for d in r1:
                firstpiece.append(a)
                firstpiece.append(b)
                firstpiece.append(c)
                firstpiece.append(d)
print(len(firstpiece))
def gen_firstpiece(n):
    return array(firstpiece[n:n+4])
secondpiece = []
for a in r1:
    for b in r1:
        secondpiece.append(a)
        secondpiece.append(b)
print(len(secondpiece))
def gen_secondpiece(n):
# En funktion som genererer den de to brikker med hver to tal. 
    return array(secondpiece[n:n+2])
def calc_lastpiece():
# Beregn de sidste fire tal.
    matrix = array([1,1,0,0,1,0,0,1,1,0,1,0,0,0,1,1]).reshape(4,4)
    vektor = array([summen - (m[2,0]+m[2,1]), summen - (m[0,0]+m[1,1]), summen - (m[0,2]+m[1,2]), summen - (m[0,3]+m[1,3])])
    return solve(matrix,vektor).reshape(2,2)
for i in range(10**4):
    m[0,0:] = gen_firstpiece(i)
# summen er det tal som alle raekker, soejler og diagonaler summerer op til.
    summen = sum(m[0,0:])
    for j in r2:
        p2 = gen_secondpiece(j)
        if m[0,0].sum() + p2.sum() <= summen:
            m[1:3,0] = p2
            m[3,0] = summen - sum(m[0:3,0])
        else:
            break
        for k in r2:
            p3 = gen_secondpiece(k)
            if m[0,1].sum() + p3.sum() <= summen:
                m[1,1:3] = p3
                m[1,3] = summen - sum(m[1,0:3])
                m[2,1] = summen - (m[0,3] + m[1,2] + m[3,0])
                m[3,1] = summen - sum(m[1,0:3])
                m[2:,2:] = calc_lastpiece()

