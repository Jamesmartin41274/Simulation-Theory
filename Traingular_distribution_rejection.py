import numpy as np 
import matplotlib.pyplot as plt 

n_sample = 10000
accepted_sample = []

while len(accepted_sample) <= n_sample:
    u = np.random.uniform(0,1)
    x = np.random.uniform(0,1)
    if u<=x:
        accepted_sample.append(x)
        
plt.hist(accepted_sample,bins=100,density = True, alpha =0.5,label= "accepted sample plot")

x_vals = np.linspace(0,1,10000)
pdf_vals = 2*x_vals

plt.plot(x_vals,pdf_vals,"r-", label="True PDF: 2x")
plt.show()