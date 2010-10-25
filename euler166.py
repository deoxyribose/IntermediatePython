from numpy import array, zeros 
from math import isnan
from numpy.linalg import solve
m = zeros((4,4))
firstpiece = []
for a in xrange(10):
    for b in xrange(10):
        for c in xrange(10):
            for d in xrange(10):
                firstpiece.append(a)
                firstpiece.append(b)
                firstpiece.append(c)
                firstpiece.append(d)
def gen_firstpiece(n):
   return array(firstpiece[n:n+4])
secondpiece = []
for a in xrange(10):
    for b in xrange(10):
        secondpiece.append(a)
        secondpiece.append(b)
def gen_secondpiece(n):
# En funktion som genererer den de to brikker med hver to tal. 
    return array(secondpiece[n:n+2])
def calc_lastpiece():
# Beregn de sidste fire tal.
    matrix = array([1,1,0,0,1,0,0,1,1,0,1,0,0,0,1,1]).reshape(4,4)
    vektor = array([summen - (m[2,0]+m[2,1]).sum(), summen - (m[0,0]+m[1,1].sum()), summen - (m[0,2]+m[1,2].sum()), summen - (m[0,3]+m[1,3].sum())])
    x = solve(matrix,vektor).reshape(2,2)
    if len([x.flatten(1)[i] for i in range(4) if x.flatten(1)[i]==abs(round(x.flatten(1)[i]))])==4:
        return x
for i in xrange(10**4):
    m[0,0:] = gen_firstpiece(i)
    summen = sum(m[0,0:])
    for j in range(100):
        p2 = gen_secondpiece(j)
        if m[0,0].sum() + p2.sum() <= summen:
            m[1:3,0] = p2
            m[3,0] = summen - sum(m[0:3,0])
        else:
            break
        for k in range(100):
            p3 = gen_secondpiece(k)
            if m[0,1].sum() + p3.sum() <= summen:
                m[1,1:3] = p3
                m[1,3] = summen - m[1,0:3].sum()
                if m[1,3] <= 0: break                    
                m[2,1] = summen - (m[0,3] + m[1,2] + m[3,0]).sum()
                if m[2,1] <= 0: break                    
                m[3,1] = summen - m[0:3,1].sum()
                if m[3,1] <= 0: break                    
                m[2:,2:] = calc_lastpiece()
                if any([any(map(isnan,r)) for r in m[2:,2:].reshape(4,1)]): break
                if i > 10:
                    print(m)
