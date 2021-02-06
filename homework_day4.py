

def division(number):
    for i in range(2,number):
        if(number%i)!=0:
            continue
        else:
            return False
    return True
        

        
        
for j in range(2,100):
    if(division(j)==True):
        print(j)
    else:
        continue




    
        
        
        
    