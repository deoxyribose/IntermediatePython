#!/usr/bin/env python
import numpy as np

n = input("Hvor mange iterationer? ")

while 1:
    vind,tab = 0,0
    skift = raw_input("Vil du skifte? y/n  ")
    for i in range(n):
# bil er en int svarende til nummeret paa den doer bag hvilken bilen er
# valg er en int svarende til nummeret paa den doer som er ens oprindelige valg
        bil = np.random.random_integers(1,3,size=1)[0]
        valg = np.random.random_integers(1,3,size=1)[0]
# Der er tre muligheder m
        m = [1,2,3]
# Den doer som vaerten skal afslore (om hvilken der gaelder at en ged skal gemme sig bag den) 
# vaelges. Det maa hverken vaere bil eller valg

# Hvis man valgte bil, kan vaerten vaelge mellem de resterende to, tilfaeldigvist.
        if valg == bil:
            m.remove(bil)
            afslorged = m[np.random.random_integers(0,1,size=1)[0]]
        else:
# Ellers er der kun den sidste mulighed.
            m.remove(valg)
            m.remove(bil)
            afslorged = m[0]
# Hvis brugeren har valgt at skifte, omdefineres valg til den sidste mulighed.
        if skift == 'y':
            m = [1,2,3]
            m.remove(afslorged)
            m.remove(valg)
            valg = m[0]
# Tjek om man har vundet.
        if bil == valg:
            vind += 1
        else:
            tab += 1
    forhold = float(vind)/(tab+vind)
    print "Du har vundet %d gange og tabt %d gange. Dvs. forholdet er %f" % (vind, tab, forhold)
