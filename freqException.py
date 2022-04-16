Input=int(input('Enter N'))
if Input<=4 and Input>=1000:
    raise Exception('N is out of range')
    
def sec(test):
    tes=test.split(' ')
    check=[]
    for i in tes:
        if i in check:
            continue
        else:
            check.append(i)
            
    if len(check)>=3:
        return True
    else:
        return False
        
Input1=input('Enter array')
if not sec(Input1):
    raise Exception('array less than 3')
    
def out(inn):
    inn=inn.split(' ')
    ctch= {}
    for i in inn:
        if i in ctch:
            ctch[i] = ctch[i] + 1
            
        else:
            ctch[i] = 1
            
    v=0
    counter =0        
    for i in ctch.values():
        if counter==0:
            v=i
            counter = 1
        elif i!=v:
            v=i
            
        else:
            continue
    z=' '
    #print(v)    
    for k in ctch.keys():
        if ctch[k] ==v:
            z=k
            break
        else:
            continue
    return(z)
    
print(out(Input1))
    
        