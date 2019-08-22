f0 = 1
f1 = 2
f2 = f0 + f1
ss = f1

while f2 <= 4000000:
    if f2%2 == 0:
        ss = ss + f2
    
    f0 = f1
    f1 = f2
    f2 = f0 + f1

print('answer is')
print(ss)
