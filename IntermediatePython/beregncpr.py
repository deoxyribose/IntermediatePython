def generercpr(p,q):
    from tjekcpr import tjekcpr
    p = int(p)
    assert p in [0,1]
    assert len(str(q)) == 6, "Skriv 6 cifre"
    antal = 0
    for i in range(4):
        for j in range(10,100):
            if p == 0:
                for k in range(0,10,2):
                    cpr = int(str(q) + str(i) + str(j) + str(k))
                    if tjekcpr(cpr) == 0:
                        print(cpr)
                        antal += 1
            else:
                for k in range(1,10,2):
                    cpr = int(str(q) + str(i) + str(j) + str(k))
                    if tjekcpr(cpr) == 0:
                        print(cpr)
                        antal += 1
    return antal
#if __name__ == '__main__':
p = input("Skriv hvor mange y-chromosomer du har (0/1): ")
q = input("Skriv din foedselsdag (ddmmyy): ")
generercpr(p,q)
print("I alt %d cpr-numre" % generercpr(p,q)) 
