import numpy as np


kp_max = 0
for i in range(100, 1000):
               for j in range(i, 1000):
                              k = i*j
                              kt = k
                              ndigit = 5
                              if(k >= 100000):
                                             ndigit = 6

                              if(ndigit == 5):
                                             k5 = k//10000
                                             kt = kt-k5*10000
                                             k4 = kt//1000
                                             kt = kt-k4*1000
                                             k3 = kt//100
                                             kt = kt-k3*100                                             
                                             k2 = kt//10
                                             kt = kt-k2*10                                                                                          
                                             k1 = kt
                                             kp = k1*10000+k2*1000+k3*100+k4*10+k5
                              elif(ndigit == 6):
                                             k6 = k//100000
                                             kt = kt-k6*100000
                                             k5 = kt//10000
                                             kt = kt-k5*10000
                                             k4 = kt//1000
                                             kt = kt-k4*1000
                                             k3 = kt//100
                                             kt = kt-k3*100                                             
                                             k2 = kt//10
                                             kt = kt-k2*10                                                                                          
                                             k1 = kt
                                             kp = k1*100000+k2*10000+k3*1000+k4*100+k5*10+k6
                              if(k == kp):
                                             print(kp)
                                             if(kp>kp_max):
                                                            kp_max = kp
print('answer is')
print(kp_max)
               
