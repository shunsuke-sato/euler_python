import numpy as np


s = 600851475143
t = int( np.ceil(np.sqrt(s)) )
flag = False

while flag == False:
    while s%t != 0:
        t = t -1

    u = 2
    while t%u != 0 and u < np.ceil(np.sqrt(t)):
        u = u + 1
        
    if u == int(np.ceil(np.sqrt(t))):
        flag = True
    else:
        t = t -1
        
    print (t)
    
print ('answer is')
print (t)
