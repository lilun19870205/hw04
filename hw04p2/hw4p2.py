import os
import time
import matplotlib.pyplot as plt
import subprocess
import numpy as np

rele_mc = 1.0
n= 3
m = 1

s = './hw04p2'
t0 = time.time()
m_i = []
relative_mp = []
relative_mc = []


while (rele_mc > 0.001):
    bash = s+' '+str(m)+' '+str(n)    
    os.system(bash)
    #subprocess.call(["./hw04p2","m","n"])
    #f = open('output.txt', 'r')
    #ans = f.read()
    #f.close()
    #ans = ans.split()
    #ans = map(float,ans)
    mystring=np.loadtxt('output.txt')
    I=mystring[0]
    I_mp=mystring[1]
    I_mc=mystring[2]
    abso_mp = abs(I_mp-I)
    rele_mp = abso_mp/I
    abso_mc = abs(I_mc-I)
    rele_mc = abso_mc/I
    m = m + 1
    m_i.append(m)
    print rele_mc
    relative_mp.append(rele_mp)
    relative_mc.append(rele_mc)
    


tend = time.time()
print tend-t0
fig1 = plt.figure(1)
plt.loglog(m_i,relative_mp)
fig1.suptitle('m vs Relative Error')
plt.xlabel('m')
plt.ylabel('Relative Error')
fig2 = plt.figure(1)
plt.loglog(m_i,relative_mc)
fig2.suptitle('m vs Relative Error')
plt.xlabel('m')
plt.ylabel('Relative Error')
plt.show()
