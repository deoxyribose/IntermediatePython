from numpy import array, zeros, vectorize 
from math import isnan
count = 1
m = zeros((4,4))
allm = [map(None,m.flatten(1))]
len_allm = [-1,0]
piece = []
piece2 = []
for a in xrange(10):
    for b in xrange(10):
        piece2.append(a)
        piece2.append(b)
        for c in xrange(10):
            for d in xrange(10):
                piece.append(a)
                piece.append(b)
                piece.append(c)
                piece.append(d)
def gen_4piece(n):
   return array(piece[n*4:(n+1)*4])
def gen_2piece(n):
    return array(piece2[n*2:(n+1)*2])
def gen_One_Piece(n):
    return array(piece3[n])
def dist_rest(Solut):
    p = -1
    for i in range(1,4):
        for j in range(i*i-5*i+7,4):
            if i+j != 6: 
                p+=1
#                print("m[%i,%i] = LinSolut[%i] = %i" %(i,j,p,LinSolut[p]))
                m[i,j] = Solut[p]
    Solut = []
def isallowed(n):
    return 0 <= n <= 9
isallowed2 = vectorize(isallowed)
def is_valid_solut(Solut):
    at_least_one_positive = any(isallowed2(Solut))
    not_all_are_zero = any(Solut) 
    none_are_negative = all(Solut == abs(Solut))
    if at_least_one_positive and not_all_are_zero and none_are_negative:
        return True
    else:
        return False
def none_are_multi_digit(Solut):
    digit_len = array([len(str(i)) -3 for i in Solut])
    if any(digit_len):
#        print(digit_len, "Some were multi-digit, next!")
        return False
    else:
        return True
def none_are_multi_digit2(Solut):
    if len([i for i in Solut if i < 10]) == len(Solut):
        return True
    else:
        return False
allsolut = []
def is_magic(np_array,s):
    if [np_array[:,i].sum() for i in range(4)] == [np_array[i,:].sum() for i in range(4)]:
        if sum([np_array[i,i].sum() for i in range(4)]) == sum([np_array[i,j].sum() for i in range(4) for j in range(4) if i+j==3]) == s:
            return True
#def is_a_multiple_of_another
if __name__ == '__main__':
    for i in xrange(10**7):
        m[0,:] = gen_4piece(i)
        s = m[0,0:].sum()
        for j in range(100):
            p2 = gen_2piece(j)
            if m[0,0].sum() + p2.sum() <= s:
                m[1:3,0] = p2
                m[3,0] = s - m[0:3,0].sum()
            else:
                break
            for k in range(10):
                p3 = k
                if m[0,1].sum() + p3 <= s:
                    m[1,1] = p3
                    LinSolut = array([-m[0,3]-m[1,2]-m[1,1]+s+m[2,0]-m[0,2]-m[0,1]+m[3,0],
                                        s-m[0,3]-m[1,2]-m[3,0],
                                        -m[1,1]-0.5*m[0,2]+0.5*m[0,3]+m[3,0]-0.5*m[0,0]+0.5*s-0.5*m[0,1],
                                        0.5*m[0,3]+m[1,2]+m[1,1]+0.5*m[0,0]-0.5*s-m[2,0]+0.5*m[0,2]+0.5*m[0,1],
                                        m[3,0]+m[1,2]-m[1,1]+m[0,3]-m[0,1],
                                        -m[1,2]+m[1,1]-0.5*m[0,2]-0.5*m[0,3]-m[3,0]+0.5*m[0,0]+0.5*s+0.5*m[0,1],
                                        -0.5*m[0,3]-m[3,0]+0.5*m[0,2]-0.5*m[0,0]+0.5*s+0.5*m[0,1]
                                        ])
                    if s != 0 and not is_valid_solut(LinSolut): break
                    if not none_are_multi_digit2(LinSolut): break
                    if (map(None,LinSolut) not in allsolut):
                        allsolut.append(map(None,LinSolut))
                    dist_rest(LinSolut)
                    if (map(None,m.flatten(1)) not in allm) and is_magic(m,s):
                        print(m)
                        allm.append(map(None,m.flatten(1)))
                        count += 1
                        if count % 100 == 0:
                            print("%i | %i" %(count,s))
                        if count > 4000:
                            print(count)
                   # print(m)
