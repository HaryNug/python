def kangaroo(x1, v1, x2, v2):
    i= 1
    if v1 < v2 or v1 == v2:
        return "No"
    if v1 > v2:
        while i < 10000 :
            if x1+v1*i== x2+v2*i:
                return "Yes"    
            i+=1
    return "No"
        # if x1+v1 == x2+v2:

            
print(kangaroo(0,3,4,2)) 