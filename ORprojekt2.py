# Intro til OR, projekt 1, opgave 13. 
# Da problemet er et dynamisk programmeringsproblem, vil en globalt optimal loesning kunne beregnes ud fra lokalt optimale loesninger. I vores tilfaelde, vil Z(4) vaere beregnet ud fra Z(3), Z(2) etc. hvor Z(i) er den billigste produktionsomkostning for ugerne 1..i. 
# Da beregningen af Z(i) kraever at man evaluerer f(i,j) (en rekursiv funktion) som flere gange indirekte (gennem kaldet af Z(i)) kalder sig selv med de samme vaerdier, cacher vi resultaterne i dict'en Zs, saa vi senere kan catche om vi behoever at kalde funktionen igen. Fx. naar man kalder Z(3), saa kaldes f(3,1), f(3,2), f(3,3), som saa kalder hhv. Z(0); Z(1); Z(0), Z(1) og Z(2), men dem har vi allerede kaldet foer - derfor behoever vi blot at slaa den rigtige vaerdi op i dict'en Zs under key i, i stedet for at beregne den igen.
# Ved samme lejlighed kan vi tjekke hvad j er (som angiver hvornaar lageret sidst var toemt), som vi kan bruge til at deducere x(i)'erne
A,h = 100,1
d = [20,50,10,50]
Zs = {0: (0,[])}
def f(i,j):
    return Z(j-1)[0] + A + h*sum([(k-j)*d[k-1] for k in xrange(j+1,i+1)])
def Z(i):
    if i not in Zs.keys():
        fs = [f(i,j) for j in xrange(1,i+1)]
        print("Z(%i) : %s" % (i, fs))
        j = fs.index(min(fs)) + 1
        Zs[i] = (min(fs), Zs[j-1][1] + [j])
    return Zs[i]
print("Den samlede produktionsomkostning er %i, og vi producerer i ugerne %s" %(Z(4)[0], " og ".join(map(str,Z(4)[1]))))
