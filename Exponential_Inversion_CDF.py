import numpy as np
from  scipy.stats import expon
import matplotlib.pyplot as plt

#The generation of 10,0000 uniform random variables
u = np.random.uniform(0,1,10000)

#Exponential distribution inversion 
X = -np.log(1-u)

#Plotting a Histogram
plt.hist(X,bins=50,density =True,alpha = 0.6,label = "Histogram of Inversion Sample points")

#Plotting the exponential function
x_vals =np.linspace(0,10,1000)
pdf_vals = expon.pdf(x_vals, scale=1) 
plt.plot(x_vals, pdf_vals, 'r-', lw=2, label='True PDF (λ=1)')

plt.title("Inverse CDF Sampling from Exponential(λ=1)")
plt.xlabel("x")
plt.ylabel("Density")
plt.legend()
plt.grid(True)
plt.show()