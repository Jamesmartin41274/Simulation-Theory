import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import expon

#sample size and uniform distribution samples from U ~ U(0,10)
n_samples = 100000

accepted_samples = [] 
while len(accepted_samples) < n_samples:
    y = np.random.uniform(0,10)
    q = np.exp(-y/2)
    u =np.random.uniform(0,1)
    if u<=q:
        accepted_samples.append(y) # accept y
        
plt.hist(accepted_samples,bins=100, density = True, alpha=0.5, label="Rejection sample plot")

x_vals = np.linspace(0,15,10000)
pdf_vals = expon.pdf(x_vals,loc=0,scale=2)
plt.plot(x_vals,pdf_vals,'r-', lw=2, label='True PDF (Exp(0.5))')
plt.title('Rejection Sampling from Exponential(λ = 0.5)')
plt.xlabel('x')
plt.ylabel('Density')
plt.legend()
plt.grid(True)
plt.show()







