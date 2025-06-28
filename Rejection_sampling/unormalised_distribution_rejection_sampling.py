import numpy as np
import matplotlib.pyplot as plt

# Define the random number generation sample size
n_samples= 100000
accepted_samples = []

#Acquiring the maximal values function
def f(x):
    return np.sin(5*x)**2 * np.exp(-x)

x_vals = np.linspace(0,np.pi,10000000)
f_vals = f(x_vals)

#supremum of the model
k=np.max(f_vals)


while len(accepted_samples) < n_samples:
    u = np.random.uniform(0,1)
    x = np.random.uniform(0, np.pi)  # Sample from proposal g(x) = Uniform(0, π)
    
    if u < f(x) / (k * (1 / np.pi)):
        accepted_samples.append(x)
        
plt.hist(accepted_samples, bins=100,density= True, alpha=0.5,label="Histogram of accepted samples")


y_vals = np.linspace(0,np.pi,1000000)
pdf_vals_unormalised = f(y_vals)
plt.plot(y_vals,pdf_vals_unormalised,'r-', lw=2, label="True PDF")
plt.legend()
plt.show()