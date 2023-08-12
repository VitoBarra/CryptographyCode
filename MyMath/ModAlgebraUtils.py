def Generate_Z_set(p):
    Z = set()
    for i in range(0, p):
        Z.add(i)
    return Z

def ModulateArray(list,p):
    for i in range(0,len(list)):
        list[i] = list[i]%p
    return list