# Problem: Resulting matrices are not magic squares.
from numpy import array, zeros 
from numpy.linalg import solve
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
def gen_firstpiece(n):
   return array(firstpiece[n:n+4])
secondpiece = []
for a in r1:
    for b in r1:
        secondpiece.append(a)
        secondpiece.append(b)
def gen_secondpiece(n):
# En funktion som genererer den de to brikker med hver to tal. 
    return array(secondpiece[n:n+2])
def calc_lastpiece():
# Beregn de sidste fire tal.
    matrix = array([1,1,0,0,1,0,0,1,1,0,1,0,0,0,1,1]).reshape(4,4)
    vektor = array([summen - (m[2,0]+m[2,1]).sum(), summen - (m[0,0]+m[1,1].sum()), summen - (m[0,2]+m[1,2].sum()), summen - (m[0,3]+m[1,3].sum())])
    return solve(matrix,vektor).reshape(2,2)
#
#
#
for i in xrange(10**10):
#    print("##########NY ITERATION#########")
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
            if m[0,1].sum() + p3.sum() <= summen and len([calc_lastpiece().flatten(1)[x] for x in range(len(calc_lastpiece().flatten(1))) if calc_lastpiece().flatten(1)[x]==abs(int(calc_lastpiece().flatten(1)[x]))])==4:
                #print('calc_lastpiece er: ', [calc_lastpiece().flatten(1)[x] for x in range(len(calc_lastpiece().flatten(1))) if calc_lastpiece().flatten(1)[x]==abs(int(calc_lastpiece().flatten(1)[x]))])
                m[1,1:3] = p3
                m[1,3] = summen - m[1,0:3].sum()
                m[2,1] = summen - (m[0,3] + m[1,2] + m[3,0]).sum()
                m[3,1] = summen - m[0:3,1].sum()
                m[2:,2:] = calc_lastpiece()
                if i > 10:
                    print(m)
                """
                print(m)
                diag1 = []
                diag2 = []
                for i in range(3):
                    print("Summen af %i'te raekke er " % i, m[i,:].sum(), "Summen af %i'te soejle er " % i, m[:,i].sum()) 
                    diag1 = sum([m[i,i] for i in range(3)])
                    diag2 = sum([m[i,j] for i in range(3) for j in range(3) if i+j == 3])
                print("Summen af forste diagonal er: ", diag1,"Summen af anden diagonal er: ", diag2)
                """
