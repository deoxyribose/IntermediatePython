def tjekcpr(n):
    assert len(str(n)) == 10
    n = str(n)
    weight = [4,3,2,7,6,5,4,3,2,1]
    kontrol = [int(n[i])*weight[i] for i in range(len(weight))]
    return sum(kontrol) % 11
if __name__ == '__main__':
    r = tjekcpr(input("Skriv cpr-nummeret: "))
    if r == 0:
        print("Det angivne cpr-nummer er gyldigt.")
    else:
        print("Det angivne cpr-nummer er ikke gyldigt.")
