def chain(s1 ="GOOD",s2 = "GIRL"):
    i,j= 0,0
    k = (len(s1) + len(s2))
    while i != k:
        if i > len(s1)-1: 
            yield s2[j]
            j += 1
        else:
            yield s1[i]
        i += 1
