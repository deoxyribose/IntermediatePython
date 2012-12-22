solut = []
s_et = 0
s_to = 0
s_tre = 0
s_fire = 0
i,j,k,l = 0,0,0,0
s = 7
for i in range(1,5):
    s_et = s - i
    for j in range(1,5):
        if s_et >= j >= 0:
            s_to = s_et - j
            for k in range(1,5):
                if s_to >= k >= 0 and i+j+k <= 7:
                    s_tre = s_to - k
                    for l in range(1,5):
                        if s_tre >= l >= 0 and i+j+k+l <=7:
                            solut.append((i,j,k,l))
verdi = []
verdin = []
verdisum = []
for i in range(len(solut)):
    verdi.append({1:1,2:3,3:6,4:8}[solut[i][0]])
    verdi.append({1:5,2:6,3:8,4:8}[solut[i][1]])
    verdi.append({1:4,2:6,3:7,4:9}[solut[i][2]])
    verdi.append({1:4,2:4,3:5,4:8}[solut[i][3]])
    verdin.append(verdi)
    verdi = []
print solut
print verdin
verdisum = [sum(x) for x in verdin]
print verdisum, max(verdisum)
print [solut[x] for x in range(len(solut)) if verdisum[x] == max(verdisum)]
