import subprocess
import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
import time
a=[]
b=[]
abs_error=1
m=10
n=1
#while(abs_error>0.001):
subprocess.call(["./hw04p2","m","n"])
mystring=np.loadtxt('output.txt')
I=mystring[0]
I_mp=mystring[1]
I_mc=mystring[2]
print mystring

print I, " ", I_mp, " ", I_mc
