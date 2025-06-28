import numpy as np
import matplotlib.pyplot as plt

#Sample numbers and accepted samples list
n_samples = 100000
accepted_samples=[]

#Target PDF 
def f(j):
    return(6*j*(1-j))

x_vals = np.linspace(0,1,1000000)
k=np.max(f(x_vals)) #max value over the target distribution since our proposal here is uniform(0,1)
print(k)

#Applying the rejection sample:

while len(accepted_samples)<n_samples:
    u = np.random.uniform(0,1) # random uniform sample value
    w = np.random.uniform(0,1) # proposal value
    if u<=f(w)/k:
        accepted_samples.append(w)
        
# Visual Aid
plt.hist(accepted_samples,bins=100,density = True, alpha = 0.5,label="rejection sample histogram")

# Actual target distribution 
plt.plot(x_vals,f(x_vals),"r-",label="Target PDF")
plt.legend()
plt.show()